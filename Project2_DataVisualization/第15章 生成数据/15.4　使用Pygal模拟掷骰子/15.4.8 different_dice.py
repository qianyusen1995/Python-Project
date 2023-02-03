from die import Die
import pygal

# 创建一个D6和一个D10
die_1 = Die()
die_2 = Die(10)

#掷几次骰子，并将结果存储在列表results中
results = []
for roll_num in range(50000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# 分析结果
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
  frequency = results.count(value)
  frequencies.append(frequency)

print(frequencies)
# 对结果进行可视化
hist = pygal.Bar()

hist.title = "Results of rolling a D6 and a D10 50,000 times."
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12',
'13', '14', '15', '16']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D10', frequencies) #传递要给添加的值指定的标签D6，还有一个列表frequencies，其中包含将出现在图表中的值
hist.render_to_file('different_visual.svg')
#hist.render_in_browser()