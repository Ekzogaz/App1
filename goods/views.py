from decimal import Context
from urllib import request
from django.shortcuts import render
from django.template import context

# Create your views here.
def catalog(request):
 
 
 return render(request,'goods/catalog.html')
 
def product(request): 
   return render(request, 'goods/product.html')