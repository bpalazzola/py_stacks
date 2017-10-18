from django.shortcuts import render, HttpResponse, redirect

from __future__ import unicode_literals
 # the index function is called when root is visited
def index(request):
    response = "Hello, I am your first request!"
    return HttpResponse(response)


