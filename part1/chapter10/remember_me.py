"""
======================
@title: remember_me
@description: 记住用户名
@author: elijah
@date: 2022/9/7 17:24
=====================
"""

import json

# 如果以前储存了用户名，就加载他
# 否则，就提醒用户输入用户名并储存它

def get_stored_username():
    """如果以前储存了用户名，就加载他"""
    filename = './../files/username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """提醒用户输入用户名"""
    username = input("what is your name? ")
    filename = './../files/username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def greet_user():
    """问候用户， 并指出其名字"""
    username = get_stored_username()
    if username:
        print("Welcome back, " + username + "!")
    else:
        username = get_new_username()
        print("We`ll remember you when you come back," + username + "!")

greet_user()