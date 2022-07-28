"""定义learning_logs的URL模式"""
from django.urls import re_path #导入了函数url ，因为我们需要使用它来将URL映射到视图

from . import views #其中的句点让Python从当前的urls.py模块所在的文件夹中导入视图。

urlpatterns = [
    # 主页 
    re_path(r'^$', views.index, name='index'), #r'^$'
] #接受三个实参,Django在urlpatterns 中查找与请求的URL字符串匹配的正则表达式