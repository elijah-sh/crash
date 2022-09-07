"""
======================
@title: name_function
@description: 测试函数
@author: elijah
@date: 2022/9/7 21:17
=====================
"""

def get_formatted_name(first, last, middle=''):
    """生成简洁的姓名"""
    if middle:
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + last

    return full_name.title()