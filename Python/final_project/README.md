Task<br>

Написать тестовое web-приложение по управлению электронной библиотекой:
1. Редактирование (доступно авторизованному пользователю при наличии аутентификации):
Управление списком книг: добавить / удалить / редактировать книгу.
Управление списком авторов: добавить / удалить / редактировать автора.
Запись о книге содержит следующие данные: ID, Название.
Запись об авторе содержит следующие данные: ID, Имя.
Свзязь между книгами и авторами — многие ко многим.
2. Поиск книг по названию либо автору (доступно анонимному пользователю при наличии аутентификации).
3. Аутентификации и авторизация (по желанию кандидата).

Task done with simple Django app and PostgreSQL RDBMS. App builds with very common pattern in web application design, MVC(Model View Controller).
In Django specificity, also know like MVT(Model View Template).
- Model, represents database level, one model describe one table from database in comfortable for programming form. 
In case django it's python class  which inherit object ```django.db.models```. 
Database level has been done with [web scraping and scripts](https://github.com/yougooo/epam_training/tree/master/Python/final_project/database) which interact with database API.
Here we define part of application logic, like 'many to many' relations. 
After this we can connect to database with Django and use  utility ```inspectdb```. 
As a result, after some modifications, have [model.py](https://github.com/yougooo/epam_training/blob/master/Python/final_project/library/books_storage/models.py).
Database 'library' contains 56099 books and 1738 authors.
![alt text](https://github.com/yougooo/epam_training/blob/master/Python/final_project/database/database_schema.png)
- View (in MVT model) generally it is methods and functions which wait for user input, extract some parameters from request, make query to models and return response to templates.
Here also define application logic, and good practice is "thin" view, fat "model". 
So this [view.py](https://github.com/yougooo/epam_training/blob/master/Python/final_project/library/books_storage/views.py) 
just for test app, more Django way use something like this: 
```python
Author.objects.get(first_name__icontains='Alex')
```
Or in database level do something like this:
```sql 
CREATE VIEW bookentry AS SELECT ... 
```
Define db view like model and work with this.
- [Template](https://github.com/yougooo/epam_training/tree/master/Python/final_project/library/templates) with DTL(Django Template Languages) take care about dynamically generation web page for user request. 
In this level used bootstrap it is html/css/js framework for easy make pretty UI. 
Common pattern for templetes it is made one 'base.html' page with ```{% block content %}``` then use it in different templates ```{% extends 'base.html' %}``` just rewrite ```{% block content %}```



