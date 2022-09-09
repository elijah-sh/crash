"""
======================
@title: number_reader
@description: 读取json文件
@author: elijah
@date: 2022/9/7 16:39
=====================
"""


import json


filename = './../files/numbers.json'
with open(filename) as f_obj:
    numbers = json.load(f_obj)

print(numbers)