from operator import index
from django import views
from django.contrib import admin
from django.urls import path

import App
from goods import views
app_name='goods'

urlpatterns = [
    path('<slug:category_slug>/', views.catalog, name='index'),
    path('product/<slug:product_slug>/',views.product, name='product'),
    
]