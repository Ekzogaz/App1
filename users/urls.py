from operator import index
from django import views
from django.contrib import admin
from django.urls import path

import App
from users import views
app_name='users'

urlpatterns = [
    path('login/',views.login, name='login'),
    path('registration/',views.registration, name='registration'),
    path('profile/',views.profile, name='profile'),
    path('users-cart/',views.users_cart, name='users_cart'),
    path('logout/',views.logout, name='logout'),

]