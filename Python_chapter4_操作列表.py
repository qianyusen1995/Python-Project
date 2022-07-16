# coding=utf-8
# P33 for 循环
jiejie = ['zhouweiwei', 'weiweizhou']
for jj in jiejie:
    print (jj.title() + ' wanna a friend.')
    print ('\t' + 'DD also wanna a friend.' + '\n')

value = tuple(range(1, 5, 2))
print (value)

square = []
for value in range(1, 6, 2):
    print(value**2)
    square.append(value**2)
print (square)
# 也可以下面一种写法，适合老手
square = [value**2 for value in range(1, 6, 2)]  # 列表解析
print (square)

print (min(square), max(square), sum(square)) #P38

# P39 切片
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print (players[0:3])
print (players[-3:])  # 负数索引
# 遍历切片
print("Here are the first three players on my team:")
for player in players[:3]:
    print (player.title())
# print (player.title for player in players)

# P40 复制列表 by 切片
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
# friend_foods = my_foods 只是赋值，和上面复制不一样
my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

# P41 4.5元组
# 元组为一系列不可修的元素；Python将不能修改的值称为不可变的；而不可变的列表被称为元组。
# 给元组变量赋值是合法的

# P42 4.6设置代码格式

