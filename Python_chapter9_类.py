#   9.1　创建和使用类
class Dog():
    """一次模拟小狗的简单尝试"""
    def __init__(self, name, age):
        """根据Dog 类创建的实例初始化属性name和age"""
        self.name = name #以self 为前缀的变量都可供类中的所有方法使用，还可以通过类的任何实例来访问这些变量
        self.age = age

    def sit(self):
        """模拟小狗被命令时蹲下"""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title() + " rolled over!")
#   9.1.2　根据类创建实例
my_dog = Dog('zora', 6)  #根据Dog类创建实例my_dog
#1.访问属性
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.") #访问与实例my_dog相关联的属性 age
#2.调用方法
my_dog.sit() #Python在类Dog 中查找方法sit() 并运行其代码。
my_dog.roll_over()
#3.创建多个实例
my_dog = Dog('willie', 6) #实例1
your_dog = Dog('lucy', 3) #实例2 可以同样的名字和年龄
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()
print("\nYour dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old.")
your_dog.sit()
#9-1 餐馆 ：创建一个名为Restaurant 的类，其方法__init__() 设置两个属性：restaurant_name 和cuisine_type 。创建一个名为describe_restaurant() 的方法和一个名为open_restaurant() 的方法，其中前者打印前述两项信息，而后者打印一条消息，指出餐馆正在营业。根据这个类创建一个名为restaurant 的实例，分别打印其两个属性，再调用前述两个方法。
class Restaurant ():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("The name of the restaurant is " + self.restaurant_name.title() + ".")
        print("The cuisine type of the restaurant is " + self.cuisine_type.title() + ".")

    def open_restaurant(self):
        print("The restaurant is now opening.")
restaurant = Restaurant("shanghai hotel", "shanghai cai")#创建实例restaurant
print("The name is " + restaurant.restaurant_name.title() + ".")
print("The cusine is " + restaurant.cuisine_type.title()  + ".")
restaurant.describe_restaurant()
restaurant.open_restaurant()
#9-2 三家餐馆 ：根据你为完成练习9-1而编写的类创建三个实例，并对每个实例调用方法describe_restaurant() 。
#9-3 用户 ：创建一个名为User 的类，其中包含属性first_name 和last_name ，还有用户简介通常会存储的其他几个属性。在类User 中定义一个名为describe_user() 的方法，它打印用户信息摘要；再定义一个名为greet_user() 的方法，它向用户发出个性化的问候。创建多个表示不同用户的实例，并对每个实例都调用上述两个方法。
class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    def describe_user(self):
        print ("The name of the user is " + self.first_name.title() + " " + self.last_name.title() + ".")

    def greet_user(self):
        print ("Welcome to Shanghai! " + self.last_name.title()+ ".")
#user1
user1 = User("liao", "huanyu")
user1.describe_user()
user1.greet_user()
#user2
user2 = User("qian", "yichen")
user2.describe_user()
user2.greet_user()
#user3
user3 = User("qian", "yichen")
user3.describe_user()
user3.greet_user()



#   9.2　使用类和实例
#   9.2.1　Car 类
#   9.2.2　给属性指定默认值
# 类中的每个属性都必须有初始值，哪怕这个值是0或空字符串。在有些情况下，如设置默认值时，在方法__init__() 内指定这种初始值是可行的；如果你对某个属性这样做了，就无需包含为它提供初始值的形参。
class Car():
    #一次模拟汽车的简单尝试
    def __init__(self, make, model, year):
        #初始化描述汽车的属性
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 #给属性odometer_reading指定默认值0

    def get_descriptive_name(self):
    #返回整洁的描述性信息
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        #打印一条指出汽车里程的消息
        print("This car has " + str(self.odometer_reading) + " miles on it.")
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
#   9.2.3　修改属性的值
class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def update_odometer(self, mileage):
        """
        2.1将里程表读数设置为指定的值
        2.2禁止将里程表读数往回调
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """将里程表读数增加指定的量"""
        """禁止增量为负值"""
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("You can't roll back an odometer!")

    def read_odometer(self):
         #打印一条指出汽车里程odometer_reading的消息
        print("This car has " + str(self.odometer_reading) + " miles on it.")
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
##  1.通过实例直接修改属性odometer_reading值为23
my_new_car.odometer_reading = 23 
my_new_car.read_odometer()
my_used_car = Car('subaru', 'outback', 2013)
print(my_used_car.get_descriptive_name())
##  2.通过方法update_odometer修改属性的值
my_used_car.update_odometer(23500) #mileage
my_used_car.read_odometer()
##  3.通过方法increment_odometer对属性odometer_reading的值递增特定的量mile
my_used_car.increment_odometer(100) #mile
my_new_car.read_odometer()
##  注意:你可以使用类似于上面的方法来控制用户修改属性值（如里程表读数）的方式，但能够访问程序的人都可以通过直接访问属性来将里程表修改为任何值。要确保安全，除了进行类似于前面的基本检查外，还需特别注意细节

#9-4就餐人数: 在为完成练习9-1而编写的程序中，添加一个名为number_served 的属性，并将其默认值设置为0。根据这个类创建一个名为restaurant 的实例；打印有多少人在这家餐馆就餐过，然后修改这个值并再次打印它。添加一个名为set_number_served() 的方法，它让你能够设置就餐人数。调用这个方法并向它传递一个值，然后再次打印这个值。添加一个名为increment_number_served() 的方法，它让你能够将就餐人数递增。调用这个方法并向它传递一个这样的值：你认为这家餐馆每天可能接待的就餐人数。
class Restaurant ():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 1

    def describe_restaurant(self):
        print("The name of the restaurant is " + self.restaurant_name.title() + ".")
        print("The cuisine type of the restaurant is " + self.cuisine_type.title() + ".")

    def open_restaurant(self):
        print("The restaurant is now opening.")

    def set_number_served(self, number):
        self.number_served = number
        print(self.number_served)
    def increment_number_served(self, increment_number):
        self.number_served += increment_number
        print(self.number_served)
restaurant = Restaurant("lanzhoulamian", "noodle")
print ("There are " + str(restaurant.number_served) + " customer eat here.")
restaurant.set_number_served(20)
restaurant.increment_number_served(5)
#9-5尝试登录次数：在为完成练习9-3而编写的User类中，添加一个名为login_attempts的属性。
# 编写一个名为increment_login_attempts()的方法，它将属性login_attempts 的值加1。
# 再编写一个名为reset_login_attempts() 的方法，它将属性login_attempts 的值重置为0。
# 根据User 类创建一个实例，再调用方法increment_login_attempts() 多次。打印属性login_attempts 的值，确认它被正确地递增；然后，调用方法reset_login_attempts() ，并再次打印属性login_attempts 的值，确认它被重置为0。
class User():
    def __init__(self, first_name, last_name, login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = login_attempts

    def  increment_login_attempts(self):
        self.login_attempts += 1
        print (self.login_attempts)

    def reset_login_attempts(self):
        self.login_attempts = 0
        print (self.login_attempts)

    def describe_user(self):
        print ("The name of the user is " + self.first_name.title() + " " + self.last_name.title() + ".")

    def greet_user(self):
        print ("Welcome to Shanghai! " + self.last_name.title()+ ".")
user1 = User("liao", "huanyu", 20)
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.reset_login_attempts()



#   9.3　继承
#   9.3.1　子类的方法__init__()
class Car(): #父类
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def update_odometer(self, mileage):
        """
        2.1将里程表读数设置为指定的值
        2.2禁止将里程表读数往回调
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """
        将里程表读数增加指定的量
        禁止增量为负值
        """
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("You can't roll back an odometer!")

    def read_odometer(self):
         #打印一条指出汽车里程odometer_reading的消息
        print("This car has " + str(self.odometer_reading) + " miles on it.")
class ElectricCar(Car): #定义子类时，必须在括号内指定父类的名称
    """电动汽车的独特之处"""
    def __init__(self, make, model, year): 
        """初始化父类的属性"""
        super().__init__(make, model, year) #函数的super()把父类Car和子类ElectricCar关联起来: 调用ElectricCar的父类的方法__init__()让子类ElectricCar的实例包含父类所有属性
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())

#   9.3.3　给子类定义属性和方法
class ElectricCar(Car): #定义子类时，必须在括号内指定父类的名称
    """电动汽车的独特之处"""
    def __init__(self, make, model, year): 
        """初始化父类的属性"""
        super().__init__(make, model, year)
        self.battery_size = 70 #添加一个电动汽车特有的属性（电瓶）存储电瓶容量 初始值70
    def describe_battery(self): #子类独有的方法
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()

#   9.3.4　重写父类的方法
class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def fill_gas_tank(self): #父类的方法fill_gas_tank
        print("This car need a gas tank!")
class ElectricCar(Car):
    def __init__(self, make, model, year): 
        """初始化父类的属性"""
        super().__init__(make, model, year)
    def fill_gas_tank(self): #重写父类的方法fill_gas_tank
        """电动汽车没有油箱"""
        print("This car doesn't need a gas tank!")
my_tesla = ElectricCar('tesla', 'model s', 2016)
my_tesla.fill_gas_tank()

#   9.3.5　将实例用作属性
class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def update_odometer(self, mileage):
        """
        2.1将里程表读数设置为指定的值
        2.2禁止将里程表读数往回调
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """
        将里程表读数增加指定的量
        禁止增量为负值
        """
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("You can't roll back an odometer!")

    def read_odometer(self):
         #打印一条指出汽车里程odometer_reading的消息
        print("This car has " + str(self.odometer_reading) + " miles on it.")
class Battery():
    """一次模拟电动汽车电瓶的简单尝试"""
    def __init__(self, battery_size=70): #如果没有给形参battery_size提供值，将被设置为70
        """初始化电瓶的属性"""
        self.battery_size = battery_size 
    def describe_battery(self): #从ElectricCar类中移过来的方法describe_battery()
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
    def get_range(self):
        """打印一条消息，指出电瓶的续航里程"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)
class ElectricCar(Car): 
    """电动汽车的独特之处"""
    def __init__(self, make, model, year): 
        """初始化父类的属性"""
        super().__init__(make, model, year) 
        """初始化电动汽车特有的属性"""
        self.battery = Battery() #创建一个新的实例Battery()，并存储在名为self.battery的属性中
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery() # 查找ElectricCar(Car)属性battery -> 找到实例Battery() -> 调用实例里的describe_battery()方法
my_tesla.battery.get_range()

#   9.3.6　模拟实物
##如何让方法get_range()将根据电瓶容量和汽车型号报告续航里程: 将方法get_range() 还留在Battery 类中，但向它传递一个参数，如car_model

# 9-6 冰淇淋小店 ：冰淇淋小店是一种特殊的餐馆。编写一个名为 IceCreamStand 的类，让它继承你为完成练习9-1或练习9-4而编写的Restaurant 类。这两个版本的Restaurant 类都可以，挑选你更喜欢的那个即可。
# 添加一个名为flavors 的属性，用于存储一个由各种口味的冰淇淋组成的列表。
# 编写一个显示这些冰淇淋的方法。创建一个IceCreamStand 实例，并调用这个方法。
class Restaurant ():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 1

    def describe_restaurant(self):
        print("The name of the restaurant is " + self.restaurant_name.title() + ".")
        print("The cuisine type of the restaurant is " + self.cuisine_type.title() + ".")

    def open_restaurant(self):
        print("The restaurant is now opening.")

    def set_number_served(self, number):
        self.number_served = number
        print(self.number_served)
    def increment_number_served(self, increment_number):
        self.number_served += increment_number
        print(self.number_served)
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["草莓味","西瓜味","奶油味"]
    def show_icecream(self):
        print (self.flavors)
McDonald_IceCreamStand = IceCreamStand("McDonald", "fast_food")
McDonald_IceCreamStand.describe_restaurant()
McDonald_IceCreamStand.show_icecream()

# 9-7 管理员 ：管理员是一种特殊的用户。编写一个名为Admin 的类，让它继承你为完成练习9-3或练习9-5而编写的User 类。
# 添加一个名为privileges 的属性，用于存储一个由字符串（如"can add post" 、"can delete post" 、"can ban user" 等）组成的列表。
# 编写一个名为show_privileges() 的方法，它显示管理员的权限。创建一个Admin 实例，并调用这个方法。
class User():
    def __init__(self, first_name, last_name, login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = login_attempts

    def  increment_login_attempts(self):
        self.login_attempts += 1
        print (self.login_attempts)

    def reset_login_attempts(self):
        self.login_attempts = 0
        print (self.login_attempts)

    def describe_user(self):
        print ("The name of the user is " + self.first_name.title() + " " + self.last_name.title() + ".")

    def greet_user(self):
        print ("Welcome to Shanghai! " + self.last_name.title()+ ".")
class Admin(User):
    def __init__(self, first_name, last_name, login_attempts):
        super().__init__(first_name, last_name, login_attempts)
        self.privileges = ["can add post", "can delete post", "can ban user"]
    def show_privileges(self):
        print (self.privileges)
HP_Admin = Admin("Daniel", "Liu", 20)
HP_Admin.describe_user()
HP_Admin.show_privileges()
# 9-8 权限 ：编写一个名为Privileges 的类，它只有一个属性——privileges ，其中存储了练习9-7 所说的字符串列表。
# 将方法show_privileges() 移到这个类中。
# 在Admin 类中，将一个Privileges 实例用作其属性。创建一个Admin 实例，并使用方法show_privileges() 来显示其权限。
class User():
    def __init__(self, first_name, last_name, login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = login_attempts

    def  increment_login_attempts(self):
        self.login_attempts += 1
        print (self.login_attempts)

    def reset_login_attempts(self):
        self.login_attempts = 0
        print (self.login_attempts)

    def describe_user(self):
        print ("The name of the user is " + self.first_name.title() + " " + self.last_name.title() + ".")

    def greet_user(self):
        print ("Welcome to Shanghai! " + self.last_name.title()+ ".")
class Admin(User):
    def __init__(self, first_name, last_name, login_attempts):
        super().__init__(first_name, last_name, login_attempts)
        self.privileges = Privileges()
class Privileges():
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]
    def show_privileges(self):
        print (self.privileges)
Jeff_Admin = Admin("Jefferson", "Qian", 20)
Jeff_Admin.describe_user()
Jeff_Admin.privileges.show_privileges()
# 9-9 电瓶升级 ：在本节最后一个electric_car.py版本中，给Battery 类添加一个名为upgrade_battery() 的方法。
# 这个方法检查电瓶容量，如果它不是85，就将它设置为85。
# 创建一辆电瓶容量为默认值的电动汽车，调用方法get_range() ，然后对电瓶进行升级，并再次调用get_range() 。你会看到这辆汽车的续航里程增加了
class Car():
    """一次模拟汽车的简单尝试"""
    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述性名称"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def update_odometer(self, mileage):
        """
        2.1将里程表读数设置为指定的值
        2.2禁止将里程表读数往回调
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """
        将里程表读数增加指定的量
        禁止增量为负值
        """
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("You can't roll back an odometer!")

    def read_odometer(self):
         #打印一条指出汽车里程odometer_reading的消息
        print("This car has " + str(self.odometer_reading) + " miles on it.")
class ElectricCar(Car): 
    """电动汽车的独特之处"""
    def __init__(self, make, model, year): 
        """初始化父类的属性"""
        super().__init__(make, model, year) 
        """初始化电动汽车特有的属性"""
        self.battery = Battery()
class Battery():
    """一次模拟电动汽车电瓶的简单尝试"""
    def __init__(self, battery_size=70): #如果没有给形参battery_size提供值，将被设置为70
        """初始化电瓶的属性"""
        self.battery_size = battery_size 
    def describe_battery(self): #从ElectricCar类中移过来的方法describe_battery()
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
    def get_range(self):
        """打印一条消息，指出电瓶的续航里程"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)
    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85
jeff_tesla = ElectricCar('tesla', 'model s', 2016)
jeff_tesla.battery.get_range()
jeff_tesla.battery.upgrade_battery()
jeff_tesla.battery.get_range()



#   9.4　导入类
#   9.4.1　导入单个类
from car import ElectricCar
#   9.4.3　从一个模块中导入多个类
from car import Car, ElectricCar
#   9.4.4　导入整个模块
import car
#   9.4.5　导入模块中的所有类(不推荐)
from module_name import *
#   9.4.6　在一个模块中导入另一个模块中必要的类
from car import Car
class ElectricCar(Car): #类ElectricCar需要访问其父类Car 
#   9.4.7　自定义工作流程
##一开始让代码结构简单： 尽可能在一个文件完成all tasks 确保一切正确运行 -> 将类移到独立的模块中
#9-10 导入Restaurant 类 ：将最新的Restaurant 类存储在一个模块中。在另一个文件中，导入Restaurant 类，创建一个Restaurant 实例，并调用Restaurant 的一个方法，以确认import 语句正确无误。

# 9-11 导入Admin 类 ：以为完成练习9-8而做的工作为基础，将User 、Privileges 和Admin 类存储在一个模块中，再创建一个文件，在其中创建一个Admin 实例并对其调用方法show_privileges() ，以确认一切都能正确地运行。

# 9-12 多个模块 ：将User 类存储在一个模块中，并将Privileges 和Admin 类存储在另一个模块中。再创建一个文件，在其中创建一个Admin 实例，并对其调用方法show_privileges() ，以确认一切都依然能够正确地运行。



#   9.5　Python标准库
from collections import OrderedDict #有序字典

favorite_languages = OrderedDict() #OrderedDict类的实例记录了键—值对的添加顺序 #favorite_languages = {}

favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
    language.title() + ".")

#9-13 使用OrderedDict ：在练习6-4中，你使用了一个标准字典来表示词汇表。请使用OrderedDict 类来重写这个程序，并确认输出的顺序与你在字典中添加键—值对的顺序一致
from collections import OrderedDict

favorate_Jay_songs = OrderedDict()

favorate_Jay_songs['twoChar'] = '晴天'
favorate_Jay_songs['threeChar'] = '七里香'
favorate_Jay_songs['fourChar'] = '千里之外'
favorate_Jay_songs['fiveChar'] = '夜的第七章'

for song_length, song_name in favorate_Jay_songs.items():
    print ("My 1st favorate song is\n" + song_name + ".\n")

#9-14 骰子 ：模块random 包含以各种方式生成随机数的函数，其中的randint() 返回一个位于指定范围内的整数，例如，下面的代码返回一个1~6内的整数：
#from random import randint
#请创建一个Die 类，它包含一个名为sides 的属性，该属性的默认值为6。
#编写一个名为roll_die() 的方法，它打印位于1和骰子面数之间的随机数。
#创建一个6面的骰子，再掷10次。 
from random import randint
class Die():
    """骰子"""
    def __init__(self, sides = 6):
        self.sides = sides

    def roll_die(self):
        """打印随机数"""
        x = randint(1, self.sides)
        print(str(x))
dice = Die()
for value in range(1,11): #循环十次
    """掷10次"""
    dice.roll_die()
#创建一个10面的骰子和一个20面的骰子，并将它们都掷10次。
dice_10 = Die(10)
for value in range(1,11): #循环十次
    """掷10次"""
    dice_10.roll_die()
dice_20 = Die(20)
for value in range(1,11): #循环十次
    """掷10次"""
    dice_20.roll_die()
#9-15 Python Module of the Week ：要了解Python标准库，一个很不错的资源是网站Python Module of the Week。请访问http://pymotw.com/ 并查看其中的目录，在其中找一个你感兴趣的模块进行探索，或阅读模块collections 和random 的文档。
