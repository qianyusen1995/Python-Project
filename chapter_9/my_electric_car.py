from electric_car import ElectricCar

my_tesla = ElectricCar('tesla', 'model s', 2016) #创建一辆电动汽车
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

