"""定义learning_logs的URL模式"""
from django.urls import re_path #导入了函数url ，因为我们需要使用它来将URL映射到视图

from . import views #其中的句点让Python从当前的urls.py模块所在的文件夹中导入视图。

urlpatterns = [
    # 主页 
    re_path(r'^$', views.index, name='index'), #r'^$'
    # 显示所有主题;接受三个实参（正则表达式，视图函数，第三个实参将这个URL模式的名称指定为index; Django在urlpatterns中查找与请求的URL字符串匹配的正则表达式
    re_path(r'^topics/$', views.topics, name='topics'),
    # 显示某一个主题的详细页面
    # ?P<topic_id> 将匹配的值存储到: 视图topic()的实参topic_id中
    # name='topic' =>topics.html {% url 'learning_logs:topic' topic.id %}
    re_path(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    # 当用户要添加新主题时，我们将切换到http://localhost:8000/new_topic/
    re_path(r'^new_topic/$', views.new_topic, name='new_topic'),
    #用于添加新条目的页面: 包含实参topic_id ，因为条目必须与特定的主题相关联
    re_path(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
    # 用于编辑条目的页面:这个URL模式将预期匹配的请求发送给视图函数edit_entry()
    re_path(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
]
