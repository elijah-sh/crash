"""
======================
@description: 读取文件
@author: elijah
@date: 2022/9/7 12:26
=====================
"""

with open('./../files/pi_digits.txt') as file_object:
    # content = file_object.read()
    # print(content)
    # print(content.strip())
    # for line in file_object:
    #     print(line.strip())
    lines = file_object.readlines()

    for line in lines:
        print(line.strip())