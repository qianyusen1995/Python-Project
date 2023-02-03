# 15.2　绘制简单的折线图
import matplotlib.pyplot as plt #模块pyplot 包含很多用于生成图表的函数
from random import choice

# 15.2.2　校正图形：
input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.plot(input_values,squares, linewidth=5) #给plot() 同时提供输入值和输出值; 参数linewidth决定了plot() 绘制的线条的粗细

# 15.2.1 修改标签文字和线条粗细:
# 15.2.1 设置图表标题，并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 15.2.1 设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=14)
plt.show()

# 15.2.5 自动计算数据
x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

# 15.2.3　使用scatter() 绘制散点图并设置其样式
# plt.scatter(2, 4, s=200) #使用实参s 设置了绘制图形时使用的点的尺寸

# 15.2.4　使用scatter() 绘制一系列点： 要绘制一系列的点，可向scatter() 传递两个分别包含x 值和y 值的列表
# 15.2.5 自动计算数据: 将输入列表和输出列表传递给scatter(); 
# 15.2.6删除数据点的轮廓: 在调用scatter() 时传递实参edgecolor='none'; 
# 15.2.7　自定义颜色: 像scatter() 传递参数c ，并将其设置为要使用的颜色的名称；
#plt.scatter(x_values, y_values, c='red', edgecolors='none', s=40)

# 15.2.8　使用颜色映射: 
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolors='none', s=40) #将参数c设置成了一个y值列表; 并使用参数cmap告诉pyplot使用哪个颜色映射: 这些代码将y值较小的点显示为浅蓝色，并将y值较大的点显示为深蓝色

# 15.2.5　自动计算数据: 设置每个坐标轴的取值范围
plt.axis([0, 1100, 0, 1100000]) # 函数axis() 要求提供四个值：x 和 y 坐标轴的最小值和最大值。在这里，我们将 x 坐标轴的取值范围设置为0~1100，并将 y 坐标轴的取值范围设置为0~1 100 000

#15.2.9　自动保存图表
#要让程序自动将图表保存到文件中，可将对plt.show() 的调用替换为对plt.savefig() 的调用：
#plt.show()
plt.savefig('squares_plot.png', bbox_inches='tight') #第一个实参指定要以什么样的文件名保存图表，这个文件将存储到scatter_squares.py所在的目录中；第二个实参指定将图表多余的空白区域裁剪掉。如果要保留图表周围多余的空白区域，可省略这个实参。


# 练习：
# 15-1 立方 ：数字的三次方被称为其立方。请绘制一个图形，显示前5个整数的立方值，再绘制一个图形，显示前5000个整数的立方值。
# 15-2 彩色立方 ：给你前面绘制的立方图指定颜色映射
# 15-3 分子运动 ：修改rw_visual.py，将其中的plt.scatter() 替换为plt.plot() 。为模拟花粉在水滴表面的运动路径，向plt.plot() 传递rw.x_values
# 和rw.y_values ，并指定实参值linewidth 。使用5000个点而不是50 000个点。
# 15-4 改进的随机漫步 ：在类RandomWalk 中，x_step 和y_step 是根据相同的条件生成的：从列表[1, -1] 中随机地选择方向，并从列表[0, 1, 2, 3, 4]
# 中随机地选择距离。请修改这些列表中的值，看看对随机漫步路径有何影响。尝试使用更长的距离选择列表，如0~8；或者将-1从 x 或 y 方向列表中删除。
# 15-5 重构 ：方法fill_walk() 很长。请新建一个名为get_step() 的方法，用于确定每次漫步的距离和方向，并计算这次漫步将如何移动。然后，
# 在fill_walk() 中调用get_step() 两次：
  # x_step = get_step()
  # y_step = get_step()
# 15-6 自动生成标签 ：请修改die.py和dice_visual.py，将用来设置hist.x_labels 值的列表替换为一个自动生成这种列表的循环。如果你熟悉列表解析，可尝试将
# die_visual.py和dice_visual.py中的其他for 循环也替换为列表解析。
# 15-7 两个D8骰子： 请模拟同时掷两个8面骰子1000次的结果。逐渐增加掷骰子的次数，直到系统不堪重负为止。
# 15-8 同时掷三个骰子 ：如果你同时掷三个D6骰子，可能得到的最小点数为3，而最大点数为18。请通过可视化展示同时掷三个D6骰子的结果。
# 15-9 将点数相乘 ：同时掷两个骰子时，通常将它们的点数相加。请通过可视化展示将两个骰子的点数相乘的结果。
# 15-10 练习使用本章介绍的两个库 ：尝试使用matplotlib通过可视化来模拟掷骰子的情况，并尝试使用Pygal通过可视化来模拟随机漫步的情况。
