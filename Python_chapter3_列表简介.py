# coding=utf-8
# Python编程：从入门到实践 第三章
# 动手试一试
from audioop import reverse
from operator import contains

guest = ['Daniel', 'Tracy', 'Scott']
print (guest)

absent_guest = guest.pop(1)
print (absent_guest + ' can not attend this dinner.')

guest.insert(1, 'Jefferson')
new_guest = guest[1]
print (new_guest + ' will attend this dinner.')
print (guest)

guest.insert(0, 'Shawn')
guest.insert(2, 'Zora')
guest.append('Jason')
print(guest)

len(guest)
print ("There are " + str(len(guest)) + " guests invited into this dinner.")

guest.pop()
print ("I am sorry, " + guest.pop() + ", we cannot invite you to this dinner.")
guest.pop()
print ("I am sorry, " + guest.pop() + ", we cannot invite you to this dinner.")
print (guest)

del guest[0]
del guest[0]
print (guest)

# P32 3.8 放眼世界
places = ['London', 'Tokyo', 'Paris', 'Roman', 'Berlin']
print ("\nHere is the places' list:")
print (places)
# sorted 暂时性排序，sort永久性排序
print (sorted(places))
print (sorted(places, reverse=True))

places.reverse()
print (places)
places.reverse()
print (places)

places.sort()
print (places)
places.sort(reverse=True)
print (places)
print (places[4]) # list out of range
# 在本章中，你学习了：列表是什么以及如何使用其中的元素；如何定义列表以及如何增删元素；如何对列表进行永久性排序，以及如何为展示列表而进行临时排序；如何确定列
# 表的长度，以及在使用列表时如何避免索引错误。
