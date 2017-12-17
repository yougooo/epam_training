from django.shortcuts import render
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.db import connection
from .models import *

def index(request):
    return render_to_response('index.html', {})



def search(request):
    print(list(request.GET.items()))
    s = "%{}%".format(list(request.GET.items())[0][0])
    with connection.cursor() as cursor:
        cursor.execute("""SELECT * FROM (SELECT (SELECT book_name
                                                 FROM book
                                                 WHERE book_entry.book_id = book.book_id),
                                                 string_agg((SELECT CONCAT(first_name, ' ', last_name)
                                                             FROM author
                                                             WHERE author.author_id = book_entry.author_id), ',') AS full_name
                                         FROM book_entry
                                         GROUP BY book_entry.book_id) AS result
                          WHERE LOWER(book_name) LIKE LOWER(%s) or
                                LOWER(full_name) LIKE LOWER(%s)""", [s,s])
        result = cursor.fetchall()
    return render_to_response('search.html', {'books':result})

