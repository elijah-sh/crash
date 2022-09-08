"""
======================
@title: settings
@description: 设置类 储存外星人入侵的所有设置类
@author: elijah
@date: 2022/9/8 15:21
=====================
"""


class Settings():
    """储存《外星人入侵》的所有设置类"""

    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
