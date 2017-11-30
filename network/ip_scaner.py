#!/usr/lib/python

# python2

import subprocess
import sys
from threading import Thread
from Queue import Queue


memo_list = [1, 2, 4, 8, 16, 32, 64, 128]

def mask_calc(subnet):
    """
    return subnet mask like list, only host part,
    looking for how many bit involved pre octet,
    mark 0 if all, if not all calc decimal representations.
    """
    sub = 32-subnet
    range_it = [0 for i in range(sub//8)]
    range_it.append(255-sum(memo_list[:sub%8])) if sub % 8 != 0 else 1
    return range_it


def hosts(address, subnet):
    """
    address::host or network, string like 192.168.1.2
    subnet:: int like /32 /24 /15 etc...
    255.255.255.255 = 32
    255 = 1 2 4 8 16 32 64 128
    11111111.11111111.11111111.11111111 = 32
    """
    ip_address = [int(part) for part in address.split('.')]
    mask = mask_calc(subnet)
    address_min = ip_address[:4-len(mask)]
    address_min.extend(mask)
    address_max = ip_address[:4-len(mask)]
    address_max.extend([255 for i in mask])
    return address_min, address_max


def ip_gen(start, end):
    """
    start::first ip address in network
    end::last ip address in network
    """
    for octet_1 in range(start[0], end[0]+1):
        for octet_2 in range(start[1], end[1]+1):
            for octet_3 in range(start[2], end[2]+1):
                for octet_4 in range(start[3], end[3]+1):
                    yield [octet_1, octet_2, octet_3, octet_4]


def ping_check(i,q):
    """
    Check available hosts in network for ping.
    """
    live_list = []
    while True:
        ip = q.get()
        ping = subprocess.call("ping -c 2 {0}".format(ip),
                               shell=True,
                               stdout=open('/dev/null', 'w'),
                               stderr=subprocess.STDOUT)
        if ping == 0:
            print("{} is alive".format(ip))
            with open('alive_ip.txt', 'a') as alive:
                alive.write(ip+'\n')
        q.task_done()


if __name__ == "__main__":

    queue = Queue()
    network, broadcast = hosts(sys.argv[1], int(sys.argv[2]))
    ips = ip_gen(network, broadcast)

    for i in range(5):
        worker = Thread(target=ping_check, args=(i,queue))
        worker.setDaemon(True)
        worker.start()

    for ip in ips:
        str_ip = '.'.join([str(octet) for octet in ip])
        queue.put(str_ip)

    queue.join()

