from die import Die
import pygal

#创建一个D6
die = Die()

#掷几次骰子，并将结果存储在列表results中
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# 分析结果
frequencies = []
for value in range(1, die.num_sides+1):
  frequency = results.count(value)
  frequencies.append(frequency)

print(frequencies)
# 对结果进行可视化
hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000 times."
hist.x_labels = ['1', '2', '3', '4', '5', '6'] #将掷D6骰子的可能结果用作 x 轴的标签
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6', frequencies) #传递要给添加的值指定的标签D6，还有一个列表frequencies，其中包含将出现在图表中的值
hist.render_to_file('die_visual.svg')
#hist.render_in_browser()
