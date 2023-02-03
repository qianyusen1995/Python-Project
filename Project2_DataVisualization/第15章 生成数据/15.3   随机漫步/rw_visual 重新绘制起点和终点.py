# 15.3.7　重新绘制起点和终点
import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
  # 15.3.3　绘制随机漫步图: 创建一个RandomWalk实例，并将其包含的点都绘制出来
  # 15.3.9　增加点数到50000，以提供更多的数据: RandomWalk实例增大num_points 的值
  rw = RandomWalk(50000) 
  rw.fill_walk()

  # 15.3.8 隐藏坐标轴
  current_axes = plt.axes()
  current_axes.xaxis.set_visible(False) #plt.axes().get_xaxis().set_visible(False)
  current_axes.yaxis.set_visible(False)  #plt.axes().get_yaxis().set_visible(False
  
  # 15.3.9 绘制点并将图形显示出来
  point_numbers = list(range(rw.num_points))
  plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=1) #在绘图时调整每个点的大小(s=15 -> s=1)
  
  # 15.3.7 突出起点和终点
  plt.scatter(0, 0, c='green', edgecolors='none', s=100)
  plt.scatter(rw.x_values[-1], rw.y_values[-1], s=100, c='red', edgecolor='none') 

  # 15.3.10　调整尺寸以适合屏幕: 设置绘图窗口的尺寸
  plt.figure(dpi=128,figsize=(10, 6))

  plt.show()
  keep_running = input("Make another walk? (y/n): ")
  if keep_running == 'n':
    break
