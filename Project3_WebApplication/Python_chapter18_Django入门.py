#Django入门 http://djangoproject.com/
# 动手试一试
#18-1 新项目 ：为更深入地了解Django做了些什么，
#创建两个空项目，看看Django创建了什么。新建一个文件夹，并给它指定简单的名称，如InstaBook或FaceGram（不要在目录learning_log中新建该文件夹），在终端中切换到该文件夹，并创建一个虚拟环境。
#在这个虚拟环境中安装Django，并执行命令 django-admin. startproject instabook .（千万不要忘了这个命令末尾的句点）。
#看看这个命令创建了哪些文件和文件夹，并与项目“学习笔记”包含的文件和文件夹进行比较。这样多做几次，直到对Django新建项目时创建的东西了如指掌。然后，将项目目录删除——如果你想这样做的话。

#18-2 简短的条目 ：当前，Django在管理网站或shell中显示Entry 实例时，模型Entry 的方法__str__() 都在它的末尾加上省略号。请在方法__str__() 中添加一条if 语句，以便仅在条目长度超过50字符时才添加省略号。使用管理网站来添加一个长度少于50字符的条目，并核实显示它时没有省略号。
def __str__(self): #方法__str__() 告诉Django，呈现条目时应显示哪些信息
    """返回模型的字符串表示"""
    if len(self.text) > 50:
        return self.text[:50] + "..." #只显示text 的前50个字符（见❺）。我们还添加了一个省略号，指出显示的并非整个条目。
    else:
        return self.text  

#18-3 Django API ：编写访问项目中的数据的代码时，你编写的是查询。请浏览有关如何查询数据的文档，其网址为https://docs.djangoproject.com/en/7.8/topics/db/queries/。其中大部分内容都是你不熟悉的，但等你自己开发项目时，这些内容会很有用。

#18-4 比萨店：新建一个名为pizzeria 的项目，并在其中添加一个名为pizzas 的应用程序。
# 定义一个名为Pizza 的模型，它包含字段name，用于存储比萨名称，如Hawaiian和Meat Lovers。
# 定义一个名为Topping 的模型，它包含字段pizza 和name，其中字段pizza 是一个关联到Pizza 的外键，而字段name 用于存储配料，如pineapple、Canadian bacon 和sausage
# 向管理网站注册这两个模型，并使用管理网站输入一些比萨名和配料。
# 使用shell来查看你输入的数据。
#a = Pizza.objects.get(id=1)

# 18-5 膳食规划程序 ：假设你要创建一个应用程序，帮助用户规划一周的膳食。为此，新建一个文件夹，并将其命名为meal_planner，再在这个文件夹中新建一个Django项目。接下来，新建一个名为meal_plans 的应用程序，并为这个项目创建一个简单的主页。

# 18-6 比萨店主页 ：在你为完成练习18-4而创建的项目Pizzeria中，添加一个主页。
