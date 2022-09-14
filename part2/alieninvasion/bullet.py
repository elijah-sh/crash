"""
======================
@title: bullet
@description: 子弹
@author: elijah
@date: 2022/9/13 22:35
=====================
"""
import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """一个对飞船发射的子弹进行管理的类"""

    def __init__(self, ai_settings, screen, ship):
        """在飞船所处的位置创键一个子弹"""
        super(Bullet, self).__init__()
        self.screen = screen

        # 在（0，0）处创建一个表示子弹的矩形，再设置正确的位置
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        if ai_settings.ship_full_fire:
            print(ai_settings.ship_full_fire_num)
            print(ai_settings.ship_full_fire_num % 2)
            if ai_settings.ship_full_fire_num % 2 == 0:
                self.rect.centerx = ship.rect.centerx - ai_settings.ship_full_fire_num
            else:
                self.rect.centerx = ship.rect.centerx + ai_settings.ship_full_fire_num
            self.rect.top = ship.rect.top - ai_settings.ship_full_fire_num
            ai_settings.ship_full_fire = False

        # 存储用小数表示的子弹位置
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """向上移动子弹"""
        # 更新表示子弹位置的小数值
        self.y -= self.speed_factor
        # 更新表示子弹的rect的位置
        self.rect.y = self.y

    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)
