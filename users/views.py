from django.shortcuts import render, redirect


def login(request):
    context: dict = {
        'title': 'Home-Авторизация'
        }
    return render(request, 'users/login.html ', context)

def registration(request):
    context: dict = {
        'title': 'Home-Регистрация'
        }
    return render(request, 'users/registration.html ', context)

def profile(request):
    context: dict = {
        'title': 'Home-Кабинет'
        }
    return render(request, 'users/profile.html ', context)

def logout(request):
    ...