#8.1 定义函数
def greet_user(username):
    """显示简单的问候语"""
    print("Hello, " + username.title() + "!")
greet_user("Jessy") #Jessy是实参

#8-1 消息 ：编写一个名为display_message() 的函数，它打印一个句子，指出你在本章学的是什么。调用这个函数，确认显示的消息正确无误。
def display_message(knowledge):
    print("In this chapter we are going to learn " + knowledge + "!")
display_message("function")
#8-2 喜欢的图书 ：编写一个名为favorite_book() 的函数，其中包含一个名为title 的形参。这个函数打印一条消息，如One of my favorite books is Alice in Wonderland 。调用这个函数，并将一本图书的名称作为实参传递给它。
def favorite_book(title):
    print("One of my favorite books is " + title +".")
favorite_book("1984")


#8.2　传递实参
#8.2.1　位置实参
def describe_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet('hamster', 'harry')
#8.2.2　关键字实参
def describe_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet(animal_type='hamster', pet_name='harry') 
describe_pet(pet_name='harry', animal_type='hamster')
#8.2.3 默认值形参
#使用默认值时，在形参列表中必须先列出没有默认值的形参，再列出有默认值的实参。这让Python依然能够正确地解读位置实参。
def describe_pet(pet_name, animal_type = 'dog'):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet(pet_name='harry')
describe_pet('harry')
#8-3 T恤 ：编写一个名为make_shirt() 的函数，它接受一个尺码以及要印到T恤上的字样。这个函数应打印一个句子，概要地说明T恤的尺码和字样。使用位置实参调用这个函数来制作一件T恤；再使用关键字实参来调用这个函数。
def make_shirt(size, typeface):
    print ("This is a shirt which is in " + size + " size and has the typeface of " + typeface + ".")
make_shirt(size = "XL", typeface = "Jessy")
#8-4 大号T恤 ：修改函数make_shirt() ，使其在默认情况下制作一件印有字样“I love Python”的大号T恤。调用这个函数来制作如下T恤：一件印有默认字样的大号T恤、一件印有默认字样的中号T恤和一件印有其他字样的T恤（尺码无关紧要）。
def make_shirt(size, typeface = "I love Python"):
    print ("This is a shirt which is in " + size + " size and has the typeface of " + typeface + ".")
make_shirt("XXL")
make_shirt(size = "XL")
make_shirt(size = "L", typeface = "Jessy")
#8-5 城市 ：编写一个名为describe_city() 的函数，它接受一座城市的名字以及该城市所属的国家。这个函数应打印一个简单的句子，如Reykjavik is in Iceland 。给用于存储国家的形参指定默认值。为三座不同的城市调用这个函数，且其中至少有一座城市不属于默认国家。
def describe_city(city_name, nation_name = "USA"):
    print (city_name + " is in " + nation_name)
describe_city("New York")
describe_city("Los Angeles")
describe_city("Tokyo", "Japan")


#8.3　返回值
#8.3.1　返回简单值
def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = first_name + ' ' + last_name
    return full_name.title() #返回到调用函数的代码行
musician = get_formatted_name('jimi', 'hendrix')
print(musician) 
#8.3.2　让实参(middle_name)变成可选的
def get_formatted_name(first_name, last_name, middle_name = ""): #Python将非空字符串解读为True
    """返回整洁的姓名"""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)
#8.3.3　返回字典
def build_person(first_name, last_name, age=''):
    """返回一个字典，其中包含有关一个人的信息"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person
musician = build_person('jimi', 'hendrix',age=27)
print(musician)
#8.3.4　结合使用函数和while 循环
def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = first_name + ' ' + last_name
    return full_name.title()
while True:
    print("\nPlease tell me your name:")
    print("(enter 'quit' at any time to quit)")
    f_name = input("First name: ")
    if f_name == 'quit':
        break
    l_name = input("Last name: ")
    if l_name == 'quit':
        break
    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")
#8-6 城市名 ：编写一个名为city_country() 的函数，它接受城市的名称及其所属的国家。这个函数应返回一个格式类似于下面这样的字符串：
#"Santiago, Chile"
#至少使用三个城市-国家对调用这个函数，并打印它返回的值。
def city_country (cityName, countryName):
    name = (cityName + ", " + countryName)
    return name.title()
Santiago = city_country("Santiago", "Chile")
print (Santiago)
Santiago = city_country("Shanghai", "China")
print (Santiago)
Santiago = city_country("Paris", "France")
print (Santiago)
#8-7 专辑 ：编写一个名为make_album() 的函数，它创建一个描述音乐专辑的字典。这个函数应接受歌手的名字和专辑名，并返回一个包含这两项信息的字典。使用这个函数创建三个表示不同专辑的字典，并打印每个返回的值，以核实字典正确地存储了专辑的信息。
#给函数make_album() 添加一个可选形参，以便能够存储专辑包含的歌曲数。如果调用这个函数时指定了歌曲数，就将这个值添加到表示专辑的字典中。调用这个函数，并至少在一次调用中指定专辑包含的歌曲数。
def make_album(singer_name, album_name, song_number =''):
    album = {'singer': singer_name, 'album': album_name}
    # work['singer'] = singer_name
    # work["album"] = album_name
    if song_number:
        album['song'] = song_number
    return album
finished_album = make_album('周杰伦', '范特西')
print(finished_album)
finished_album = make_album('王力宏', '火力全开')
print(finished_album)
finished_album = make_album('林俊杰', '江南', song_number=13)
print(finished_album)
#8-8 用户的专辑 ：在为完成练习8-7编写的程序中，编写一个while 循环，让用户输入一个专辑的歌手和名称。获取这些信息后，使用它们来调用函数make_album() ，并将创建的字典打印出来。在这个while 循环中，务必要提供退出途径。
def make_album(singer_name, album_name, song_number =''):
    album = {'singer': singer_name, 'album': album_name}
    if song_number:
        album['song'] = song_number
    return album
while True:
    print("\nPlease type your favorate singer:")
    print("Enter 'quit' at any time to quit: ")
    s_name = input("singer name: ")
    if s_name == 'quit':
        break
    a_name = input("album name: ")
    if s_name == 'quit':
        break
    s_number = input("song number: ")
    if s_number == 'quit':
        break
    made_album = make_album(s_name, a_name)
    print (made_album)
    print ("My favorite singer is " + s_name.title() + ".")
print (made_album)


#8.4　传递列表
def greet_users(names):
    """向列表names中的每位用户name都发出简单的问候"""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)
usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)
#8.4.1　在函数中修改列表
#一家为用户提交的设计制作3D打印模型的公司。需要打印的设计存储在一个列表中，打印后移到另一个列表中
def print_models(unprinted_designs, completed_models):
    """
    模拟打印每个设计，直到没有未打印的设计为止
    打印每个设计后,都将其移到列表completed_models中
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        # 模拟根据设计制作3D打印模型的过程
        print("Printing model: " + current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """显示打印好的所有模型"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
#8.4.2　禁止函数修改列表
##可向函数传递列表的副本而不是原件，这样函数所做的任何修改都只影响副本，而丝毫不影响原件
print_models(unprinted_designs[:], completed_models)
#8-9 魔术师 ：创建一个包含魔术师名字的列表，并将其传递给一个名为show_magicians() 的函数，这个函数打印列表中每个魔术师的名字。
def show_magicians(magicians):
    for magician in magicians:
        print (magician.title())
magicians = ['zora', 'jeff']
show_magicians(magicians)
#8-10 了不起的魔术师 ：在你为完成练习8-9而编写的程序中，编写一个名为make_great() 的函数，对魔术师列表进行修改，在每个魔术师的名字中都加入字样“the Great”。调用函数show_magicians() ，确认魔术师列表确实变了。
def show_magicians(magicians):
    for magician in magicians:
        print (magician.title()) 

def make_great(magicians):
    for i in range(len(magicians)):  
        magicians[i] = "the Great " + magicians[i]
    return magicians

magicians = ['余美玲', '钱宇森','王力晗','钟熠']
show_magicians(magicians)

great_magicians = make_great(magicians)
show_magicians(great_magicians)
#8-11 不变的魔术师 ：修改你为完成练习8-10而编写的程序，在调用函数make_great() 时，向它传递魔术师列表的副本。由于不想修改原始列表，请返回修改后的 列表，并将其存储到另一个列表中。分别使用这两个列表来调用show_magicians() ，确认一个列表包含的是原来的魔术师名字，而另一个列表包含的是添加了字样“the Great”的魔术师名字。
def show_magicians(magicians):
    for magician in magicians:
        print (magician.title()) 
def make_great(magicians):
    for i in range(len(magicians)):  
        magicians[i] = "the Great " + magicians[i]
    return magicians

magicians = ['余美玲', '钱宇森','王力晗','钟熠']
magicians_copy = magicians[:]

show_magicians(magicians)
great_magicians = make_great(magicians_copy)
show_magicians(great_magicians)


#   8.5　传递任意数量的实参
def make_pizza(*toppings):
    """概述要制作的比萨"""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
#8.5.1　结合使用位置实参和任意数量实参
def make_pizza(size, *toppings): #如果要让函数接受不同类型的实参，必须在函数定义中将接纳任意数量实参的形参放在最后
    """概述要制作的比萨"""
    print("\nMaking a " + str(size) +
        "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
#   8.5.2　使用任意数量的关键字实参
def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    profile = {} #创建一个名为profile 的空字典，用于存储用户简介
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items(): #遍历字典user_info 中的键—值对
        profile[key] = value #并将每个键—值对都加入到字典profile （不管额外提供了多少个键—值对都可以运行）
    return profile #将字典profile 返回给函数调用行
user_profile = build_profile('albert', 'einstein',
location='princeton',field='physics') 
print(user_profile)
#8-12 三明治 ：编写一个函数，它接受顾客要在三明治中添加的一系列食材。这个函数只有一个形参（它收集函数调用中提供的所有食材），并打印一条消息，对顾客点的三明治进行概述。调用这个函数三次，每次都提供不同数量的实参。
def sandwich(*ingredients):
    print ("\nThis is the ingredients as per your wish: ")
    for ingredient in ingredients:
        print ('-' + ingredient)
sandwich('onion','cucumber','potato')
#8-13 用户简介 ：复制前面的程序user_profile.py，在其中调用build_profile() 来创建有关你的简介；调用这个函数时，指定你的名和姓，以及三个描述你的键-值对。
def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    profile = {} #创建一个名为profile 的空字典，用于存储用户简介
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items(): #遍历字典user_info 中的键—值对
        profile[key] = value
    return profile 

user_profile = build_profile('albert', 'einstein',
location='princeton',field='physics',hobby='badminton') 
print(user_profile)
#8-14 汽车 ：编写一个函数，将一辆汽车的信息存储在一个字典中。这个函数总是接受制造商和型号，还接受任意数量的关键字实参。这样调用这个函数：提供必不可少的信息，以及两个名称—值对，如颜色和选装配件。这个函数必须能够像下面这样进行调用：
#car = make_car('subaru', 'outback', color='blue', tow_package=True)
#打印返回的字典，确认正确地处理了所有的信息
def make_car(producer, model, **car_info):
    car = {}
    car["producer:"] = producer
    car["model:"] = model
    for key, value in car_info.items():
        car[key] = value
    return car #不能忘记返回值: 返回的是原本设置的空字典car

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)
#   8.6　将函数存储在模块中
##将函数存储在被称为模块 的独立文件中，再将模块导入到主程序中
#   8.6.1　导入整个模块
import chapter_8.printing_functions
#   8.6.2　导入特定的函数
from chapter_8.printing_functions import print_models
#   8.6.3　使用as 给函数指定别名
from chapter_8.printing_functions import print_models as pm # from module_name import function_name1, function_name2 as fn1, fn2
#   8.6.4　使用as 给模块指定别名
import chapter_8.printing_functions as pf
#   8.6.5　导入模块中的所有函数
from chapter_8.printing_functions import * #可通过名称来调用每个函数，而无需使用句点表示法
 


#   8.7　函数编写指南： https://peps.python.org/pep-0008/
#8-15   打印模型 ：将示例print_models.py中的函数放在另一个名为printing_functions.py的文件中；在print_models.py 的开头编写一条import 语句，并修改这个文件 以使用导入的函数。
#导入整个模块as pf
import chapter_8.printing_functions as pf
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
pf.print_models(unprinted_designs, completed_models)
#调用模块pf里的函数
from chapter_8.printing_functions import print_models as pm, show_completed_models as scm
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
pm(unprinted_designs, completed_models)
scm(completed_models)

#8-16 导入 ：选择一个你编写的且只包含一个函数的程序，并将这个函数放在另一个文件中。在主程序文件中，使用下述各种方法导入这个函数，再调用它：
# import module_name
# from module_name import function_name
# from module_name import function_name as fn
# import module_name as mn
# from module_name import *