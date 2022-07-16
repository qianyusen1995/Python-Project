# coding=utf-8
# 5.4　使用if 语句处理列表1  P50  
# if-elif-else

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.") # 比萨店的青椒用完了
    else:
        print("Adding " + requested_topping + ".")
print("Finished making your pizza!")

# 5.4　使用if 语句处理列表2 
requested_toppings = []

if requested_toppings == "":
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
    print("\nFinished making your pizza!")
else:
    print("\nAre you sure you want a plain pizza?")

# 动手试一试

# 5.5 设置if 语句的格式 
    # 在诸如== 、>= 和<= 等比较运算符两边各添加一个空格: if age < 4: 要比if age<4: 好   
    # 自己的想法 ：与刚拿起本书时相比，现在你是一名能力更强的程序员了。鉴于你对如何在程序中模拟现实情形有了更深入的认识，你可以考虑使用程序来解决一些问题。随着编程技能不断提高，你可能想解决一些问题，请将这方面的想法记录下来。想想你可能想编写的游戏、想研究的数据集以及想创建的Web应用程序。