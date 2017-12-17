# Rolling releases with Ansible

Your task is creating an ansible playbook that manages zero-downtime deployment of a sample Node.js application.

## Setting up
Provided `Vagrantfile` defines 5 boxes by default:
* A `command` box from which you will run ansible (hostname: command, ip: 10.0.15.10)
* A `lb` box that will serve as load balancer (hostname: lb, ip: `10.0.15.11`)
* 3 `app` boxes (`app1`, `app2`, `app3`) that will serve the application itself (hostname: appN, ip: 10.0.15.2N)

Your initial task is:
* Set up a `nginx` or `haproxy` load balancer
* Deploy [sample Node.js application](https://bitbucket.org/ZaRDaK/devops-rolling-release) to app servers
* Wire everything up

## Rolling release
1. Take app server off load balancer
2. Stop the application
3. Update the application
4. Start the application
5. Ensure the application started correctly
6. Add app server to load balancer

If any step fails, abort the whole play

To test this, use `ab` command to simulate many requests while deploying:
```bash
ab -n <Toal number of requests> -c <Number of concurrent requests> <Load balancer ip>
```

## Solutions

![alt text](http://makescreen.ru/i/e13e8977aa0b929f4053984f72f66d.png)

For task used google cloud. 

#### Step 1. Ensure all depends packages for deploy app, in deployment environments are present

Role appserver task [app_deps.yml](https://github.com/yougooo/epam_training/blob/master/IaC/rolling-release/site/roles/appservers/tasks/app_deps.yml) take care for this.

For default in deb repo nodejs version is 4.x, but for app required >= 7.0.0 node.

```yml
- name: ensure nodejs version in deb repo
  apt_repository:
          repo: "{{ item }}"
          state: present
  with_items:
          - "deb https://deb.nodesource.com/node_7.x stretch main"
          - "deb-src https://deb.nodesource.com/node_7.x stretch main"

- name: update deb repo
  apt:
update_cache: yes
```
Nodemon care about changes in app code and restart node. Because just supervisor for reload node process not enough. 

```yml
- name: ensure nodemon
  npm:
          name: nodemon
          global: yes
          production: yes
state: present
```
#### Step 2. Clone app from repo, start and ensure app will be up after reboot or shutdown system or any others crashs.

Do this with role appservers task [main.yml](https://github.com/yougooo/epam_training/blob/master/IaC/rolling-release/site/roles/appservers/tasks/main.yml).

Supervisor take control under app process, and take care for start app when system is booting. For each app server ensure supervisor config is present, with [supervisor.j2](https://github.com/yougooo/epam_training/tree/master/IaC/rolling-release/site/roles/appservers/templates) conf. 
```yml
- name: ensure supervisor conf
  template:
          src: supervisor.j2
          dest: /etc/supervisor/conf.d/app.conf
```

#### Step 3. Configure loadbalancer

For this step used nginx like simple balancer. Role loadbalancer task [main.yml](https://github.com/yougooo/epam_training/blob/master/IaC/rolling-release/site/roles/loadbalancer/tasks/main.yml) take appservers in upstream with templates upstream.j2. 

```
upstream balancer{
          {% for host in groups['appservers'] %}
                server {{ hostvars[host]['ansible_host'] }};
          {% endfor %}
}
```

After step 3 [loadbalancer](http://35.198.155.215/) start working.


#### Step 4. Update app version
App version define in [defaults](https://github.com/yougooo/epam_training/blob/master/IaC/rolling-release/site/roles/release/defaults/main.yml) with others role variables. When update in processing drop host from balancer upstream. 
```yml
- name: drop host from blancer list
  template:
          src: curr_upstream.j2
          dest: /etc/nginx/conf.d/default.conf
  delegate_to: 'lb'

- name: reload nginx
  service:
          name: nginx
          state: reloaded
  delegate_to: 'lb'
```
templates curr_upstream.j2, like Django templates.
```
upstream balancer{
          {% for host in groups['appservers'] %}
                {% if host != inventory_hostname  %}
                    server {{ hostvars[host]['ansible_host'] }};
                {% endif %}
          {% endfor %}
}
```
After update if all ok and app port responds, restore upstream. If something fall down stop apps update. 

#### Step 5. Run ansible playbook

[app_deploy.yml](https://github.com/yougooo/epam_training/blob/master/IaC/rolling-release/site/app_deploy.yml) for deploy app and up loadbalancer 

[release.yml](https://github.com/yougooo/epam_training/blob/master/IaC/rolling-release/site/release.yml) for update version in repo we have 3(v1.0.0, v1.1.0(broken),v2.0.0(current))
