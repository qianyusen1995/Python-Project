"""为应用程序users定义URL模式"""
from django.urls import re_path
from django.contrib.auth.views import LoginView #导入默认登录视图
from . import views

urlpatterns = [
  # 登录页面 http://localhost:8000/users/login
  re_path(r'login/',LoginView.as_view(template_name='users/login.html'),name='login'),
  re_path(r'logout/', views.logout_view, name='logout'),
  #与URL http://localhost:8000/users/register/匹配，并将请求发送给我们即将编写的函数register()
  re_path(r'^register/$', views.register, name='register'),
]