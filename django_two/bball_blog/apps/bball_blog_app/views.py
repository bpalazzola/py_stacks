# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return render(request, 'bball_temp/index.html')

def home_page(request):
    return render(request, 'bball_temp/home_page.html')

def my_profile(request):
    return render(request, 'bball_temp/my_profile.html')

def products(request):
    return render(request, 'bball_temp/products.html')
