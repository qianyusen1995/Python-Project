import csv
from datetime import datetime
from matplotlib import pyplot as plt

# 从文件中获取最高气温
filename = 'death_valley_2014.csv' #sitka_weather_2014.csv & sitka_weather_07-2014.csv
with open(filename) as f:
  reader = csv.reader(f)
  header_row = next(reader)
  # print(header_row)
  # for index, column_header in enumerate(header_row):
  #   print(index, column_header)

  dates, highs, lows = [], [], []
  for row in reader:
    try:
      current_date=datetime.strptime(row[0], "%Y-%m-%d")
      high = int(row[1])
      low = int(row[3])
    except ValueError:
      print(current_date, 'missing data')
    else:
      dates.append(current_date)
      # print(dates)
      highs.append(high)
      # print(highs)
      lows.append(low)

# 根据数据绘制图形
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5) #将最高气温列表high传给plot()
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# 设置图形的格式
title = "Daily high and low temperatures - 2014\nDeath Valley, CA"
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()

# 16-1 旧金山 ：旧金山的气温更接近于锡特卡还是死亡谷呢？请绘制一个显示旧金山最高气温和最低气温的图表，并进行比较。可从http://www.wunderground.com/history/
# 下载几乎任何地方的天气数据。为此，请输入相应的地方和日期范围，滚动到页面底部，找到名为Comma-Delimited File的链接，再单击该链接，将数据存储为CSV文件。
# 16-2 比较锡特卡和死亡谷的气温 ：在有关锡特卡和死亡谷的图表中，气温刻度反映了数据范围的不同。为准确地比较锡特卡和死亡谷的气温范围，需要在y 轴上使
# 用相同的刻度。为此，请修改图16-5和图16-6所示图表的y 轴设置，对锡特卡和死亡谷的气温范围进行直接比较（你也可以对任何两个地方的气温范围进行比较）。你
# 还可以尝试在一个图表中呈现这两个数据集。
# 16-3 降雨量 ：选择你感兴趣的任何地方，通过可视化将其降雨量呈现出来。为此，可先只涵盖一个月的数据，确定代码正确无误后，再使用一整年的数据来运行它。
# 16-4 探索 ：生成一些图表，对你好奇的任何地方的其他天气数据进行研究。