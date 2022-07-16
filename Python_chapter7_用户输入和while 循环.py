#7.1 让程序暂停运行，等待用户输入一些文本
greetings = "My name is: "
greetings += "\nWhat's your name? "
name = input(greetings)
print (name)


#7.2　while 循环简介

#7.2.1　使用while 循环
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:  #如果结果为0（意味着current_number 可被2整除），就执行continue 语句，让Python忽略余下的代码，
        continue 
    print(current_number)
#7.2.2 让用户选择何时退出 quit
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program1. "
message = ""
while message != 'quit':
    message = input(prompt)

    if message != 'quit': #程序在显示消息前将做简单的检查: 仅在消息不是退出值时才打印它
        print(message)
#7.2.3　使用标志: 定义一个变量active，用于判断整个程序是否处于活动状态。这个变量被称为标志
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program2. "
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)
#7-4 比萨配料 ：编写一个循环，提示用户输入一系列的比萨配料，并在用户输入'quit' 时结束循环。每当用户输入一种配料后，都打印一条消息，说我们会在比萨中添加这种配料。
prompt = "\nPlease choose the sauce that you like:"
prompt += "\nEnter 'quit' to end the menu. "
message = ""
while message != 'quit':
    message = input(prompt)
    print ("We will add " + message + " into the menu.")
# 7-5 电影票 ：有家电影院根据观众的年龄收取不同的票价：不到3岁的观众免费；3~12岁的观众为10美元；超过12岁的观众为15美元。请编写一个循环，在其中询问用户的年龄，并指出其票价。
# 7-6 三个出口 ：以另一种方式完成练习7-5，在程序中采取如下所有做法。
# 7-6 在while 循环中使用条件测试来结束循环。
ticket = "Please input your age to buy the ticket: "
ticket += "\nEnter quit to quit the window."
age = ""
while age != "quit":
    age = input(ticket)
    if age == "quit":
        print ("Thank you. You have quited the system.")
    elif int(age) < 3: 
        print ("You ticket fee is free.")
    elif int(age)>=3 and int(age)<=12:
        print ("You ticket fee is 10 dollar.")
    else:
        print ("You ticket fee is 15 dollar.")
# 7-6 使用变量active 来控制循环结束的时机。
ticket = "Please input your age to buy the ticket: "
ticket += "\nEnter quit to quit the window."
age = ""
active = True
while active:
    age = input(ticket)
    if age == "quit":
        active = False
        print ("Thank you. You have quited the system.")
    elif int(age) < 3: 
        print ("You ticket fee is free.")
    elif int(age)>=3 and int(age)<=12:
        print ("You ticket fee is 10 dollar.")
    else:
        print ("You ticket fee is 15 dollar.") 
# 7-6 使用break 语句在用户输入'quit' 时退出循环。
ticket = "Please input your age to buy the ticket: "
ticket += "\nEnter quit to quit the window."
age = ""
while age != "quit":
    age = input(ticket)
    if age == "quit":
        print ("Thank you. You have quited the system.")
        break
    else:
        if int(age) < 3: 
            print ("You ticket fee is free.")
        elif int(age)>=3 and int(age)<=12:
            print ("You ticket fee is 10 dollar.")
        else:
            print ("You ticket fee is 15 dollar.") 


#7.3　使用while 循环来处理列表和字典

#7.3.1 在列表之间移动元素：
## 首先，创建一个待验证用户列表
## 和一个用于存储已验证用户的空列表
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
## 验证每个用户，直到没有未验证用户为止
## 将每个经过验证的列表都移到已验证用户列表中
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)
## 显示所有已验证的用户
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
#7.3.2　删除包含特定值的所有列表元素
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)
#7.3.3　使用用户输入来填充字典
## 设置一个空字典
responses = {}
## 设置一个标志，指出调查是否继续
polling_active = True
while polling_active:
## 提示输入被调查者的名字和回答
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
## 将答卷存储在字典中
    responses[name] = response
## 看看是否还有人要参与调查
    repeat = input("Would you like to let another person respond? (yes/ no) ")
if repeat == 'no':
    polling_active = False
## 调查结束，显示结果
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")
# 7-8 熟食店 ：创建一个名为sandwich_orders 的列表，在其中包含各种三明治的名字；再创建一个名为finished_sandwiches 的空列表。遍历列表sandwich_orders ，对于其中的每种三明治，都打印一条消息，如I made your tuna sandwich ，并将其移到列表finished_sandwiches 。所有三明治都制作好后，打印一条消息，将这些三明治列出来。
sandwich_orders = ["zora","kami","chenye",'pastrami']
finished_sandwiches = []
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print ("I made your tuna sandwich: " + current_sandwich + ".")   
    finished_sandwiches.append(current_sandwich)

print ("\nBelow sandwich has been finished:")
for finished_sandwich in finished_sandwiches:
    print (finished_sandwich)
# 7-9 五香烟熏牛肉（pastrami）卖完了 ：使用为完成练习7-8而创建的列表sandwich_orders ，并确保'pastrami' 在其中至少出现了三次。在程序开头附近添加这样的代码：打印一条消息，指出熟食店的五香烟熏牛肉卖完了；再使用一个while 循环将列表sandwich_orders 中的'pastrami' 都删除。确认最终的列表finished_sandwiches 中不包含'pastrami' 。
print ("熟食店的五香烟熏牛肉卖完了")
sandwich_orders = ["zora","kami","chenye",'pastrami','pastrami','pastrami']
finished_sandwich = []
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    finished_sandwich.append(sandwich)
    #finished_sandwich.append(sandwich_orders.pop())
print(finished_sandwich)
# 7-10 梦想的度假胜地 ：编写一个程序，调查用户梦想的度假胜地。使用类似于“If you could visit one place in the world, where would you go?”的提示，并编写一个打印调查结果的代码块。
print ("---Questionare for holiday site---")
dreamed_holiday_sites = {}
active = True
while active:
    name = input("What is your name? ")
    dreamed_holiday_site = input("If you could visit one place in the world, where would you go? ")
    dreamed_holiday_sites[name] = dreamed_holiday_site
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        active = False

print("\n---Answers to the questionaire---")
for name, dreamed_holiday_site in dreamed_holiday_sites.items():
    print (name + "'s dreamed holiday site is " + dreamed_holiday_site +".")