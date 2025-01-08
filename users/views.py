from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import auth, messages
from django.contrib.auth import login as auth_login
from django.http import HttpResponseRedirect
from .forms import ProfileForm, UserLoginForm, UserRegistrationForm


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                messages.success(request, 'Вы успешно вошли в аккаунт')

                if request.POST.get('next', None):
                    return HttpResponseRedirect(request.POST.get('next'))
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
                form.save()
                user = form.instance
                auth_login(request, user)
                messages.success(request,f"{user.username}, 'Вы успешно зарегистрированны и вошли в аккаунт")
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserRegistrationForm()
    context: dict = {
        'title': 'Home-Регистрация',
        'form': form 
    }
    return render(request, 'users/registration.html ', context)
@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(
            data=request.POST, 
            files=request.FILES,
            instance=request.user
        )
        if form.is_valid():
            form.save()
            messages.success(request, 'Профиль успешно обновлен')
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = ProfileForm(instance=request.user)
    
    context = {
        'title': 'Home-Личный кабинет',
        'form': form
    }
    return render(request, 'users/profile.html', context)

@login_required
def logout(request):
    messages.success(request,f"{request.user.username}, 'Вы вышли из аккаунта")
    auth.logout(request)
    return redirect(reverse('main:index'))