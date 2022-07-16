"""(模块级文档字符串)一个可用于表示餐厅的类"""

class Restaurant ():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 1

    def describe_restaurant(self):
        print("The name of the restaurant is " + self.restaurant_name.title() + ".")
        print("The cuisine type of the restaurant is " + self.cuisine_type.title() + ".")

    def open_restaurant(self):
        print("The restaurant is now opening.")

    def set_number_served(self, number):
        self.number_served = number
        print(self.number_served)
    def increment_number_served(self, increment_number):
        self.number_served += increment_number
        print(self.number_served)