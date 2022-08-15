"""learning_log URL Configuration

The `urlpatterns` list routes URLs to views. 
    For more information please see: https://docs.djangoproject.com/en/4.0/topics/http/urls/

Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, re_path
from django.contrib import admin

urlpatterns = [
    #该模块admin.site.urls定义了可在管理网站中请求的所有URL。
    re_path('admin/', admin.site.urls),
    #这行代码与任何以单词users打头的URL（如http://localhost:8000/users/login/）都匹配;
    re_path(r'users/', include(('users.urls','users'))), #命名空间'users'
    re_path(r'', include(('learning_logs.urls','learning_logs'))),
]