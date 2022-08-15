from django.shortcuts import render

from .models import Pizza

# Create your views here.
def index(request):
    """主页"""
    return render(request, 'pizzas/index.html')

def pizzas(request): #request: Django从服务器那里收到的request 对象
    """显示所有的主题"""
    pizzas = Pizza.objects.order_by('date_added') #查询数据库——请求提供Topic对象
    context = {'pizzas': pizzas} #定义一个将要发送给模板的上下文:键是我们将在模板中用来访问数据的名称，而值是我们要发送给模板的数据
    return render(request, 'pizzas/pizzas.html', context) #将对象request, 模板的路径，变量context传递给render()

def pizza(request, pizza_id): 
    """显示单个主题及所有的条目"""
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.topping_set.order_by('-date_added')
    context = {'pizza': pizza, 'toppings':toppings}
    return render(request, 'pizzas/pizza.html', context)