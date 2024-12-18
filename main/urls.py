from operator import index
from django import views
from django.contrib import admin
from django.urls import path

import App
from main import views
app_name='main'

urlpatterns = [
    path('',views.index, name='index'),
    path('about/',views.about, name='about'),
]