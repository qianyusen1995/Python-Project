#15.3.3　绘制随机漫步图 ~ 15.3.4　模拟多次随机漫步
import matplotlib.pyplot as plt #模块pyplot 包含很多用于生成图表的函数
from random_walk import RandomWalk 

# 只要程序处于活动状态，就不断地模拟随机漫步
while True:
# 创建一个RandomWalk实例，并将其包含的点都绘制出来
  rw = RandomWalk() #创建了一个RandomWalk 实例
  rw.fill_walk()

  point_numbers = list(range(rw.num_points)) #使用了range() 生成了一个数字列表，其中包含的数字个数与漫步包含的点数相同(其中包含各点的先后顺序)
  plt.scatter(rw.x_values, rw.y_values, s=15, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none') #随机漫步包含的x和y值传递给scatter(); 选择了点尺寸15(s=15); 将参数c设置为point_numbers; 指定使用颜色映射Blues; 传递实参edgecolor=none 以删除每个点周围的轮廓; 
  plt.show()
  
  keep_running = input("Make another walk? (y/n): ")
  if keep_running == 'n':
    break


