#编写一个函数，它接受两个形参：一个城市名和一个国家名。这个函数返回一个格式为City, Country 的字符串，如Santiago, Chile。将这个函数存储在一个名为city_functions.py的模块中。
def city_functions(cityname, countryname, population = ""):
    if population:#population不为空字符串
        formatted_name = cityname.title() + " " + countryname.title() + " - population " + population
    else:#population为空字符串
        formatted_name = cityname.title() + " " + countryname.title()
    return formatted_name
