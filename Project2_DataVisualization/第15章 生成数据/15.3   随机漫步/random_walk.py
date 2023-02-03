# 15.3.1 创建RandomWalk() 类
from random import choice

class RandomWalk():
  """一个生成随机漫步数据的类"""
  def __init__(self, num_points=5000):
    """初始化随机漫步的属性"""
    self.num_points = num_points
    
    # 所有随机漫步都始于(0, 0)
    self.x_values = [0]
    self.y_values = [0]

  # 15.3.2　选择方向
  def fill_walk(self):
      """计算随机漫步包含的所有点"""
      # 不断漫步，直到列表达到指定的长度
      while len(self.x_values) < self.num_points:
         
        # 决定前进方向以及沿这个方向前进的距离
        x_direction = choice([1, -1]) #要么是表示向右走的1，要么是表示向左走的-1
        x_distance = choice([0, 1, 2, 3, 4]) #通过包含0，我们不仅能够沿两个轴移动，还能够沿y轴移动。
        x_step = x_direction * x_distance
        y_direction = choice([1, -1])
        y_distance = choice([0, 1, 2, 3, 4])
        y_step = y_direction * y_distance
      
        # 拒绝原地踏步
        if x_step == 0 and y_step == 0:
          continue
        # 计算下一个点的x和y值
        next_x = self.x_values[-1] + x_step #将x_step 与x_values 中的最后一个值（-1）相加
        next_y = self.y_values[-1] + y_step
        self.x_values.append(next_x)
        self.y_values.append(next_y)
