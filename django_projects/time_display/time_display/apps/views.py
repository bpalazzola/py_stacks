# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request);
    return HttpResponse("<h1>This is Brian Palazzolas Homepage</h1>")