from django.shortcuts import render

# Create your views here.
def index(request):
    """主页"""
    return render(request, 'pizzas/index.html')