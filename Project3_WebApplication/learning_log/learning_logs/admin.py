from django.contrib import admin

# Register your models here.
from learning_logs.models import Topic, Entry

admin.site.register(Topic) #让Django通过 管理网站 管理我们的模型。
admin.site.register(Entry)