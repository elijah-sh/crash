## chapter11 测试代码



## 测试代码

### 1、测试函数

 

name_function.py

```python
def get_formatted_name(first, last):
    """生成简洁的姓名"""
    full_name = first + ' ' + last
    return full_name.title()
```



names.py 用户输入名和姓

```python
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
```



> python标准库中的模块unttest提供代码测试工具
>
> 良好的测试用例考虑到了函数可能收到的各种输入
>
> 对于大型项目，要实现全覆盖可能很难，通常只针对代码重要行为编写测试即可



test_name_function.py 测试单元

```python
import unittest
from name_function import get_formatted_name

class NameTestCase(unittest.TestCase):
    """测试name_function.py"""

    def test_first_last_name(self):
        """能够正确地处理像Janis Joplin这样的名字吗?"""
        formatted = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted, 'Janis Joplin')

unittest.main()
```



创建NameTestCase类，只包含一个方法，运行test_name_function.py时，以test打头的方法都将字段运行。

unittest类最常见功能 断言方法，来核实得到的结果是否与期望的结果一致

一致时输入的结果



```

----------------------------------------------------------------------
Ran 0 tests in 0.000s

OK

Process finished with exit code 0

Empty suite

```



失败时 输出结果不同



```
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
PS C:\Users\shenshuaihu\code\PycharmProjects\crash>  py .\part1\chapter11\test_name_function.py
F
======================================================================
FAIL: test_first_last_name (__main__.NameTestCase)
能够正确地处理像Janis Joplin这样的名字吗?
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\code\PycharmProjects\crash\part1\chapter11\test_name_function.py", line 19, in test_first_last_name
    self.assertEqual(formatted, 'Janis Joplin77')
AssertionError: 'Janis Joplin' != 'Janis Joplin77'
- Janis Joplin
+ Janis Joplin77
?             ++


----------------------------------------------------------------------
Ran 1 test in 0.001s

FAILED (failures=1)

```





更改name_function.py参数时

```
def get_formatted_name(first, middle, last):
    """生成简洁的姓名"""
    full_name = first + ' ' + middle + '' + last
    return full_name.title()
```





```
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
PS C:\Users\shenshuaihu\code\PycharmProjects\crash>  py .\part1\chapter11\test_name_function.py
F
======================================================================
FAIL: test_first_last_name (__main__.NameTestCase)
能够正确地处理像Janis Joplin这样的名字吗?
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\shenshuaihu\code\PycharmProjects\crash\part1\chapter11\test_name_function.py", line 19, in test_first_last_name
    self.assertEqual(formatted, 'Janis Joplin77')
AssertionError: 'Janis Joplin' != 'Janis Joplin77'
- Janis Joplin
+ Janis Joplin77
?             ++


----------------------------------------------------------------------
Ran 1 test in 0.001s

FAILED (failures=1)
PS C:\Users\code\PycharmProjects\crash>  py .\part1\chapter11\test_name_function.py
E
======================================================================
ERROR: test_first_last_name (__main__.NameTestCase)
能够正确地处理像Janis Joplin这样的名字吗?
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\shenshuaihu\code\PycharmProjects\crash\part1\chapter11\test_name_function.py", line 18, in test_first_last_name
    formatted = get_formatted_name('janis', 'joplin')
TypeError: get_formatted_name() missing 1 required positional argument: 'last'

----------------------------------------------------------------------
Ran 1 test in 0.001s

FAILED (errors=1)

```





---

调查问卷测试

survey.py  匿名调查类

```python
"""
======================
@title: survey
@description: 匿名调查类
@author: elijah
@date: 2022/9/7 22:36
=====================
"""

class AnonymousSurvey():
    """手机匿名调查问卷的答案"""

    def __init__(self, question):
        """储存一个问题，并为存储答案做准备"""
        self.question = question
        self.responses = []

    def show_question(self):
        """显示调查问卷"""
        print(self.question)

    def store_response(self, new_response):
        """存储单份调查答案"""
        self.responses.append(new_response)

    def show_resulte(self):
        """显示收集到的所以答案"""
        print("Survey results:")
        for respones in self.responses:
            print("- " + respones)
```



language_survey.py 语言调查

```python
"""
======================
@title: language_survey
@description: 调查问卷
@author: elijah
@date: 2022/9/7 22:52
=====================
"""

from survey import AnonymousSurvey

# 定义一个问题，并创建一个表示调查的AnonymousSurvey对象
question = "What language did you first learn to speak?"
my_servey = AnonymousSurvey(question)

# 显示问题并储存答案
my_servey.show_question()
print("Enter `q` at any time to quit.\n")
while True:
    resource = input("Language: ")
    if resource == 'q':
        break
    my_servey.store_response(resource)

# 显示调查结果
print("\nThank you to everyone who participated in the survey!")
my_servey.show_resulte()
```



测试用例

```python
"""
======================
@title: test_survey
@description: 测试问卷用例
@author: elijah
@date: 2022/9/7 23:00
=====================
"""

import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """针对AnonymousSurvey类的测试"""


"""
======================
@title: test_survey
@description: 测试问卷用例
@author: elijah
@date: 2022/9/7 23:00
=====================
"""

import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """针对AnonymousSurvey类的测试"""



    def test_store_single_response(self):
        """测试单个答案会被妥善地储存"""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')

        self.assertIn('English', my_survey.responses)

    def test_store_three_response(self):
        """测试三个答案会被妥善地储存"""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        respones = ['English', 'Spanish', 'Chinese']
        for respone in respones:
            my_survey.store_response(respone)

        for respone in respones:
            self.assertIn(respone, my_survey.responses)


unittest.main
```





##### 方法setUp()

创建对象



import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """针对AnonymousSurvey类的测试"""



```ptyhon
# def test_store_single_response(self):
#     """测试单个答案会被妥善地储存"""
#     question = "What language did you first learn to speak?"
#     my_survey = AnonymousSurvey(question)
#     my_survey.store_response('English')
#
#     self.assertIn('English', my_survey.responses)
#
# def test_store_three_response(self):
#     """测试三个答案会被妥善地储存"""
#     question = "What language did you first learn to speak?"
#     my_survey = AnonymousSurvey(question)
#     respones = ['English', 'Spanish', 'Chinese']
#     for respone in respones:
#         my_survey.store_response(respone)
#
#     for respone in respones:
#         self.assertIn(respone, my_survey.responses)

def setUp(self):
    """
    创建一个调查对象和一组答案， 供使用的测试方法使用
    :return:
    """
    question = "What language did you first learn to speak?"
    self.my_survey = AnonymousSurvey(question)
    self.response = ['English', 'Spanish', 'Chinese']

def test_store_single_response(self):
    """测试单个答案会被妥善地储存"""
    self.my_survey.store_response(self.response[0])
    self.assertIn('English', self.my_survey.responses)

def test_store_three_response(self):
    """测试三个答案会被妥善地储存"""
    for respone in self.response:
        self.my_survey.store_response(respone)

    for respone in self.response:
        self.assertIn(respone, self.my_survey.responses)
```



更为简洁的测试， 解决重复问题



> 测试也是为了减少对项目的破坏
>
> 如果你编写的代码通过了测试，其他程序员也更远和你合作



```
2022/09/07
成都封锁一周整
3天+3天
现在来看遥遥无期
或者和上海一年，成都人也无法做自己的主了...
```

