from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import auth
from django.contrib.auth import login as auth_login
from django.http import HttpResponseRedirect
from .forms import UserLoginForm, UserRegistrationForm


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm()
    
    context: dict = {
        'title': 'Home-Авторизация',
        'form': form
        }
    return render(request, 'users/login.html', context)

def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
                user = form.save()
                auth_login(request, user)
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserRegistrationForm()
    context: dict = {
        'title': 'Home-Регистрация',
        'form': form 
    }
    return render(request, 'users/registration.html ', context)

def profile(request):
    context: dict = {
        'title': 'Home-Кабинет'
        }
    return render(request, 'users/profile.html ', context)

def logout(request):
    auth.logout(request)
    return redirect(reverse('main:index'))