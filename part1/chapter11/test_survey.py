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

unittest.main