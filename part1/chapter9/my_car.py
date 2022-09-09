"""
======================
@description: 我的车 导入类练习
@author: elijah
@date: 2022/9/6 23:28
=====================
"""

from car import Car
from electric_car import ElectricCar

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()


my_beetle = Car('voleswagen', 'beetle', 2022)
print(my_beetle.get_descriptive_name())



my_tesla = Car('tesla', 'roadster', 2022)
print(my_tesla.get_descriptive_name())

