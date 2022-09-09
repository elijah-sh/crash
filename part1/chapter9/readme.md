## chapter9 类

## 9.1 创建和使用类

### 9.1.1 创建Dog类

dog.py
```python

```
init方法
创建实例

### 9.2 使用类和实例

car.py

```python

"""
======================
@author:elijah
@time:2022/9/6:14:50
=====================
默认属性
修改属性
"""


class Car():
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        # 历程 默认值
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """打印一条汽车里程"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """
        将里程表读数设置为指定的值
        禁止将里程表读数往回调
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("Your can`t roll back an odometer!")

    def increment_odometer(self, miles):
        """将里程表读数增加指定的量"""
        self.odometer_reading += miles


my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(23)
my_new_car.read_odometer()


my_used_car = Car('subaru', 'outback', 2013)
print(my_used_car.get_descriptive_name())
my_used_car.update_odometer(23500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()
```

默认属性
修改属性


### 9.3 继承

electric_car.py

```python

import car


class ElectricCar(car.Car):
    """电动汽车的独特之处"""

    def __init__(self, make, model, year):
        """
        初始化父类的属性
        再初始化电动汽车特有的属性
        """
        super().__init__(make, model, year)
        self.battery_size = 70

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + "-kwh battery")


my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
```

重写父类的方法

#### 9.4 导入类

导入单个类和多个类

my_car，py

```python
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


```

一个模块导入另一个模块
