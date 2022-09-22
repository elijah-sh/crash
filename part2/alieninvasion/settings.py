"""
======================
@title: settings
@description: 设置类 储存外星人入侵的所有设置类
@author: elijah
@date: 2022/9/8 15:21
=====================
"""
import pygame


class Settings():
    """储存《外星人入侵》的所有设置类"""

    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 1000
        self.screen_height = 700
        # 灰 230, 230, 230 蓝 R:0 G:191 B:243
        self.bg_color = (0, 191, 243)
        self.bg_image = 'images/stars.bmp'

        # 飞船的设置
        self.ship_speed_factor = 6.5
        self.ship_full_fire = False
        self.ship_full_fire_num = 7
        self.ship_limit = 3

        # 子弹的设置
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 255, 0, 0

        self.bullets_allowed = 77777777777777777

        # 外星人设置
        self.alien_speed_factor = 20
        self.fleet_drop_speed = 10
        # fleet_direction 为1表示向右移 -1表示向左移动
        self.fleet_direction = 1



