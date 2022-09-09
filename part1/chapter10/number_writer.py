"""
======================
@title: number_writer
@description:
@author: elijah
@date: 2022/9/7 16:14
=====================
"""

import json

numbers = [2, 3, 5, 7, 11, 13]

filename = './../files/numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)