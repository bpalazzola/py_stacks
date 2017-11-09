from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^home_page$', views.home_page),
    url(r'^my_profile$', views.my_profile),
    url(r'^products$', views.products),
]
