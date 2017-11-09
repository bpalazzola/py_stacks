# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from time import gmtime, strftime
from datetime import datetime
from pytz import all_timezones


def today():
    date_now = strftime('%b %d, %Y %I:%M %p')
    for zone in all_timezones:
        if 'US/Central' in zone:
            print zone
            return date_now


def index(request):  # @app.route is like request
    the_date_today = today()
    print the_date_today
    context = {
        "the_date_today": the_date_today,
    }

    return render(request, "time_temp/index.html", context)