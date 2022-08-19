from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse #from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from .models import Topic, Entry #导入了与所需数据相关联的模型
from .forms import TopicForm, EntryForm


# Create your views here.
def index(request):
    """学习笔记的主页"""
    return render(request, 'learning_logs/index.html')

@login_required
def topics(request): #request: Django从服务器那里收到的request对象
    """显示所有的主题"""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added') #查询数据库——请求提供Topic对象
    context = {'topics': topics} #定义一个将要发送给模板的上下文: 键是我们将在模板中用来访问数据的名称，值是我们要发送给模板的数据
    return render(request, 'learning_logs/topics.html', context) #将对象request, 模板的路径，变量context传递给render()


@login_required
#这个函数接受正则表达式(?P<topic_id>\d+)捕获的值，并将其存储到topic_id中
def topic(request, topic_id): 
    """显示单个主题及所有的条目"""
    topic = Topic.objects.get(id=topic_id)

    #确认请求的主题属于当前用户
    check_topic_owner(request, topic)

    # date_added前面的减号指定按降序排列，即先显示最近的条目;通过外键关系获取数据，可使用相关模型entry的小写名称、下划线和单词set
    entries = topic.entry_set.order_by('-date_added')

    # 主题topic &条目entries；键是我们将在模板中用来访问数据的名称，值是我们要发送给模板的数据
    context = {'topic': topic, 'entries':entries} 
    return render(request, 'learning_logs/topic.html', context)

@login_required
def new_topic(request):
    """添加新主题"""
    if request.method != 'POST':
        # 未提交数据：创建一个新表单
        form = TopicForm()
    else:
        # POST提交的数据,对数据进行处理
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user #新主题的owner 属性设置为当前用户
            new_topic.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

@login_required
def new_entry(request, topic_id): #定义包含形参topic_id, 用于存储从URL中获得的值
    topic = Topic.objects.get(id=topic_id)
    check_topic_owner(request, topic)
    if request.method != 'POST':
        # 未提交数据：创建一个空表单
        form = EntryForm()
    else:
        # POST提交的数据,对数据进行处理
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False) #让Django创建一个新的条目对象new_entry,不将它保存到数据库中
            new_entry.topic = topic #将new_entry的属性topic设置为在这个函数开头从数据库中获取的主题
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic_id])) #重定向调用reverse()需要两个实参：1.要根据它来生成URL的URL模式的名称topic；2.列表args ，其中包含要包含在URL中的所有实参
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    """编辑既有条目"""
    entry = Entry.objects.get(id=entry_id) #获取用户要修改的条目对象，
    topic = entry.topic #以及与该条目相关联的主题
    check_topic_owner(request, topic)
    if request.method != 'POST':
        # 初次请求，使用当前条目填充表单
        form = EntryForm(instance=entry) #使用实参instance=entry 创建一个EntryForm 实例instance
    else:
        # POST提交的数据，对数据进行处理
        form = EntryForm(instance=entry, data=request.POST) #处理POST请求时，传递实参instance=entry 和 data=request.POST
        if form.is_valid(): #检查表单是否有效
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic.id])) #重定向到显示条目所属主题的页面topic.html
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)

def check_topic_owner(request, topic): 
    if topic.owner != request.user:
        raise Http404  
