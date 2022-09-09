"""
======================
@title: background 背景图
@description:
@author: elijah
@date: 2022/9/9 10:28
=====================
"""

import pygame


class Background():

    def __init__(self, screen):
        """初始化飞船并设置其初始值位置"""
        self.screen = screen

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/stars.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将图片铺满屏幕
        self.rect.center = self.screen_rect.center
        # self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)



