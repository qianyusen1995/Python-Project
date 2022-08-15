from pyexpat import model
from django.db import models

# Create your models here.
# 定义一个名为Pizza 的模型，它包含字段name，用于存储比萨名称，如Hawaiian和Meat Lovers。
# 定义一个名为Topping 的模型，它包含字段pizza 和name，其中字段pizza 是一个关联到Pizza 的外键，
# 而字段name 用于存储配料，如pineapple、Canadian bacon 和sausage
class Pizza(models.Model):
    name = models.CharField(max_length=20)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        """返回模型的字符串表示"""
        return self.name
        
class Topping(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
