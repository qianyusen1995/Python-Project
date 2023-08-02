import json
import pygal_maps_world.maps
from country_codes import get_country_code
from pygal.style import LightColorizedStyle as LCS, RotateStyle as RS

# 将数据加载到一个列表中
filename = 'population_data.json'
with open(filename) as f:
  pop_data = json.load(f)

# 创建一个包含人口数量的字典
cc_populations = {}
# 打印每个国家2010年的人口数量
for pop_dict in pop_data: #将每个字典依次存储在pop_dict 中
  if pop_dict['Year'] == '2010':
    country_name = pop_dict['Country Name']
    population = int(float(pop_dict['Value']))
    code = get_country_code(country_name)
    if code:
      cc_populations[code] = population #print(code + ": " + str(population))
    # else:
    #   print('ERROR - ' + country_name)

# 根据人口数量将所有的国家分成三组
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_populations.items():
  if pop < 10000000:
    cc_pops_1[cc] = pop
  elif pop < 1000000000:
    cc_pops_2[cc] = pop
  else:
    cc_pops_3[cc] = pop

# 看看每组分别包含多少个国家
print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))

# wm_style = RotateStyle('#336699')
# wm_style = LightColorizedStyle
wm_style = RS('#336699', base_style=LCS)
#wm_style = RotateStyle('#336699', base_style=LightColorizedStyle)
wm = pygal_maps_world.maps.World(style=wm_style)

wm.title = 'World Population in 2010, by Country'

# wm.add('2010', cc_populations)
wm.add('0-10m', cc_pops_1)
wm.add('10m-1bn', cc_pops_2)
wm.add('>1bn', cc_pops_3)
wm.render_to_file('world_population.svg')


# 16-5 涵盖所有国家 ：本节制作人口地图时，对于大约12个国家，程序不能自动确定其两个字母的国别码。请找出这些国家，在字典COUNTRIES 中找到它们的国别
# 码；然后，对于每个这样的国家，都在get_country_code() 中添加一个if-elif 代码块，以返回其国别码：
  # if country_name == 'Yemen, Rep.'
  # return 'ye'
  # elif --snip--
# 将这些代码放在遍历COUNTRIES 的循环和语句return None 之间。完成这样的修改后，你看到的地图将更完整。
# 16-6 国内生产总值 ：Open Knowledge Foundation提供了一个数据集，其中包含全球各国的国内生产总值（GDP），可在http://data.okfn.org/data/core/gdp/ 找到这个数据
# 集。请下载这个数据集的JSON版本，并绘制一个图表，将全球各国最近一年的GDP呈现出来。
# 16-7 选择你自己的数据 ：世界银行（The World Bank）提供了很多数据集，其中包含有关全球各国的信息。请访问http://data.worldbank.org/indicator/ ，并找到一个你感
# 兴趣的数据集。单击该数据集，再单击链接Download Data并选择CSV。你将收到三个CSV文件，其中两个包含字样Metadata，你应使用第三个CSV文件。编写一个程
# 序，生成一个字典，它将两个字母的Pygal国别码作为键，并将你从这个文件中选择的数据作为值。使用Worldmap 制作一个地图，在其中呈现这些数据，并根据你的
# 喜好设置这个地图的样式。
# 16-8 测试模块country_codes ：我们编写模块country_codes 时，使用了print 语句来核实get_country_code() 能否按预期那样工作。请利用你在第11
# 章学到的知识，为这个函数编写合适的测试。