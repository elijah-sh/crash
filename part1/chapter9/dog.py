"""
======================
@author:elijah
@time:2022/9/6:9:48
=====================
"""


class Dog():
    """一次模拟小狗的简单尝试"""

    def __init__(self, name, age):
        """初始化属性name和age"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗被命令时蹲下"""
        print(self.name.title() + " is now siting.")

    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title() + " rolled over")


my_dog = Dog('willie', 6)
your_dog = Dog('Lucy', 3)

print("My dog`s name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()
my_dog.roll_over()


your_dog.sit()
your_dog.roll_over()