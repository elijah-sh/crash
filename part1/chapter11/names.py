"""
======================
@title: names
@description: 用户输入名和姓
@author: elijah
@date: 2022/9/7 21:19
=====================
"""

from name_function import get_formatted_name

print("Enter `q` at any time to quit.")
while True:
    first = input('\nPlease give me a first name: ')
    if first == 'q':
        break
    last = input('\nPlease give me a last name: ')
    if last == 'q':
        break

    formmatted_name = get_formatted_name(first, last)
    print("\tNeatly formatted name: " + formmatted_name + '.')