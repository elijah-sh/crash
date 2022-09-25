"""
======================
@title: alien_invasion
@description: 外星人入侵游戏项目
@author: elijah
@date: 2022/9/8 11:35
=====================
"""

import sys
import pygame
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建Play按钮
    play_button = Button(ai_settings, screen, "Play")

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)

    # 创建储存子弹的编组
    bullets = Group()

    # 一个外星人编组
    aliens = Group()

    # 创建一个外星人
    # alien = Alien(ai_settings, screen)

    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 创建一个用于储存游戏统计信息的实例
    stats = GameStats(ai_settings)

    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        gf.check_event(ai_settings, screen, stats, play_button, ship, bullets, aliens)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, bullets, aliens)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

        gf.update_screen(ai_settings, stats, screen, ship, aliens, bullets, play_button)


run_game()
