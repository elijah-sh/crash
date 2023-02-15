"""
======================
@title: scoreboard
@description: 记分类 用于显示最高得分、等级和余下的飞船数
@author: elijah
@date: 2022/12/23 16:24
=====================
"""
import pygame.font
from pygame.sprite import Group
from ship import Ship


class Scoreboard:
    """显示得分信息的类"""

    def __init__(self, ai_settings, screen, stats):
        """初始化显示得分涉及的属性"""
        self.score_image = None
        self.score_rect = None
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # 显示得分信息时使用的字体设置
        self.text_color = (30, 30, 30)
        self.text_white_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 30)

        # 准备初始得分图像
        self.prep_score()
        # 最高分和当前得分
        self.prep_high_score()

        # 等级
        self.prep_level()
        # 飞船剩余数量
        self.prep_ships()

    def prep_score(self):
        """将得分转换一幅渲染的图像"""
        rounded_score = int(round(self.stats.score, -1))
        score_str = "Score: " + "{:,}".format(rounded_score)

        # score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_white_color)

        # 将得分放在屏幕右上角
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 10
        self.score_rect.top = self.screen_rect.top

    def show_score(self):
        """在屏幕上显示得分"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)

        # 绘制飞船
        self.ships.draw(self.screen)

    def prep_high_score(self):
        """将最高得分转换为渲染等图像"""
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = "Hight Score: " + "{:,}".format(high_score)

        # , self.ai_setting.bg_color
        self.high_score_image = self.font.render(high_score_str, True, self.text_white_color)

        """将最高得分放在屏幕顶部中央"""
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.right = self.score_rect.right - 600
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        """将等级转换为渲染的图像"""
        self.level_image = self.font.render("Level: " + str(self.stats.level), True, self.text_white_color)

        # 将等级放在得分下方
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        """显示还剩余多少艘飞船"""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_settings, self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)
