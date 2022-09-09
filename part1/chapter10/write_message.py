"""
======================
@title: write_message
@description: 写入数据到文本
@author: elijah
@date: 2022/9/7 14:52
=====================
"""

filename = './../files/programming.txt'

# with open(filename, 'w') as file_object:
#     file_object.write("I love programming.\n")
#     file_object.write("I love creating new games.\n")

with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large  darasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")