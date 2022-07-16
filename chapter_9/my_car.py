from car import Car
from electric_car import ElectricCar

# my_new_car = Car('audi', 'a4', 2016)
# print(my_new_car.get_descriptive_name())
# my_new_car.odometer_reading = 23
# my_new_car.read_odometer()

my_beetle = Car('volkswagen', 'beetle', 2016) 
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2016) #创建一辆电动汽车
print(my_tesla.get_descriptive_name())

