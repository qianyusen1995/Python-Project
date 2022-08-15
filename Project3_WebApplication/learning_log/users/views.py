# Create your views here.
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate #导入了默认视图login
from django.contrib.auth.forms import UserCreationForm

def logout_view(request): 
    """注销用户"""
    logout(request)#调用函数logout() ，它要求将request对象作为实参
    return HttpResponseRedirect(reverse('learning_logs:index')) #重定向到主页

def register(request):
    """注册新用户"""
    if request.method != 'POST':
        # 显示空的注册表单
        form = UserCreationForm()
    else:
        # 处理填写好的表单
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            # 让用户自动登录，再重定向到主页
            authenticated_user = authenticate(username=new_user.username,
            password=request.POST['password1']) #我们知道输入的这两个密码是相同的，因此可以使用其中任何一个:password1
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('learning_logs:index'))

    #通过上下文字典将这个表单发送给模板
    context = {'form': form} 
    return render(request, 'users/register.html', context)