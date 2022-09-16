"""
======================
@title: alien
@description: 外星人
@author: elijah
@date: 2022/9/16 22:46
=====================
"""

import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """表示单个外星人的类"""

    def __init__(self, ai_settings, screen):
        """初始化外星人并设计起始位置"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载外星人图像， 并设计其rect属性
        self.image = pygame.image.load('./images/alien.bmp')
        self.rect = self.image.get_rect()

        # 每个外形人最初位置都在屏幕左上角附件
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 储存外星人的准确位置
        self.x = float(self.rect.x)

    def blitme(self):
        """在指定位置绘制外星人"""
        self.screen.blit(self.image, self.rect)
