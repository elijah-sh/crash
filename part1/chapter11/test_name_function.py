"""
======================
@title: test_name_function
@description: 单元测试
@author: elijah
@date: 2022/9/7 21:29
=====================
"""

import unittest
from name_function import get_formatted_name

class NameTestCase(unittest.TestCase):
    """测试name_function.py"""

    def test_first_last_name(self):
        """能够正确地处理像Janis Joplin这样的名字吗?"""
        formatted = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted, 'Janis Joplin')

    def test_first_last_middle_name(self):
        """能够正确地处理像Wolfgang Amadeus Mozart这样的名字吗？"""
        formatted = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted, 'Wolfgang Amadeus Mozart')

unittest.main()