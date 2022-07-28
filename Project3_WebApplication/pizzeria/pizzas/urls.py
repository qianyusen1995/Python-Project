"""定义pizzas的URL模式"""
from django.urls import re_path

from . import views

urlpatterns = [
    #homepage
    re_path(r'^$', views.index, name = 'index')
]