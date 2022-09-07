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
