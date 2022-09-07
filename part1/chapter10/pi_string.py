"""
======================
@title: pi_string
@description: 读数并使用文件内容
@author: elijah
@date: 2022/9/7 14:35
=====================
"""

filename = './../files/pi_million_digits.txt'


with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi!")


