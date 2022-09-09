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
