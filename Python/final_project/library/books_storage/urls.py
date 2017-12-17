from django.conf.urls import url
from django.contrib import admin
from .views import *


urlpatterns = [
    url(r'home/$', index, name='index'),
    url(r'^home/search/$', search, name='search'),]