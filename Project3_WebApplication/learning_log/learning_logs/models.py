from django.db import models
# Create your models here.
class Topic(models.Model): #继承了Model: Django中一个定义了模型基本功能的类
    """用户学习的主题"""
    text = models.CharField(max_length=200) #属性text是一个CharField————由字符或文本组成的数据,存储少量的文本；必须告诉Django该在数据库中预留多少空间
    date_added = models.DateTimeField(auto_now_add=True) #每当用户创建新主题时，这都让Django将这个属性自动设置成当前日期和时间。
    def __str__(self):#Django调用方法__str__() 来显示模型的简单表示
        """返回模型的字符串表示"""
        return self.text #返回存储在属性text 中的字符串

class Entry(models.Model): #Entry 也继承了Django基类Model
    """学到的有关某个主题的具体知识"""
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE) #属性topic 是一个ForeignKey的实例，将条目与主题关联起来 
    ##django 升级到2.O 以后，表之间的关联，必现写上on_delete 参数
    text = models.TextField() # 属性text是一个TextField实例
    date_added = models.DateTimeField(auto_now_add=True) # 属性date_added 让我们能够按创建顺序呈现条目，并在每个条目旁边放置时间戳。
    class Meta: #Meta 类 存储用于管理模型的额外信息
        verbose_name_plural = 'entries'
    def __str__(self): #方法__str__() 告诉Django，呈现条目时应显示哪些信息
        """返回模型的字符串表示"""
        if len(self.text) > 50:
            return self.text[:50] + "..." #只显示text 的前50个字符（见❺）。我们还添加了一个省略号，指出显示的并非整个条目。
        else:
            return self.text
    