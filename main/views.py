from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    context={
        'title': 'Home',
        'content': 'Главная страница магазина' ,
        'list': ['First','Second'] ,
        'dict': {'first' : 1} ,
        'Boolean': True  ,
    }

    return render(request,'main/index.html', context)
def about(request):
    return HttpResponse('About page')

