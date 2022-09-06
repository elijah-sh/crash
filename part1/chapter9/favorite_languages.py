"""
======================
@description: 喜欢的语言
@author: elijah
@date: 2022/9/6 23:38
=====================
"""

from collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages['jen'] = 'python'
favorite_languages['echo'] = 'java'
favorite_languages['elijah'] = 'python'
favorite_languages['julianna'] = 'c'

for name, language in favorite_languages.items():
    print(name.title() + "`s favorite languages is " + language.title() + '.')