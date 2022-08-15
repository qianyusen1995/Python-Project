"""定义pizzas的URL模式"""
from django.urls import re_path

from . import views

urlpatterns = [
    #homepage
    re_path(r'^$', views.index, name='index'),#第三个实参将这个URL模式的名称指定为index，让我们能够在代码的其他地方引用它。每当需要提供到这个主页的链接时，我们都将使用这个名称，而不编写URL。
    re_path(r'^pizzas/$', views.pizzas, name='pizzas'), 

    re_path(r'^pizzas/(?P<pizza_id>\d+)/$', views.pizza, name='pizza'),  
]