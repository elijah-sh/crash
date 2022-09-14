"""
======================
@title: game_functions
@description: 游戏方法
@author: elijah
@date: 2022/9/9 10:10
=====================
"""

import pygame
import sys
from bullet import Bullet


def check_event(ai_settings, screen, ship, bullets):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            print("键盘事件： " + str(event.key))
            check_keydown_event(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_event(event, ship)


def check_keydown_event(event, ai_settings, screen, ship, bullets):
    """键盘按下"""
    if event.key == pygame.K_RIGHT:
        # 向右移动飞船
        # ship.rect.centex += 1
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True

    if event.key == pygame.K_SPACE:
        # 创建一颗子弹， 并将其加入到编组bullets中
        fire_bullet(ai_settings, screen, ship, bullets)
    if event.key == pygame.K_RETURN:
        # 加大活力
        fire_full_bullet(ai_settings, screen, ship, bullets)


def check_keyup_event(event, ship):
    """键盘松开"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False


def update_screen(ai_settings, screen, ship, bullets):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环时都重绘制屏幕
    screen.fill(ai_settings.bg_color)

    # 添加背景
    bg_image = pygame.image.load(ai_settings.bg_image).convert()
    screen.blit(bg_image, (0, 0))

    # 在飞船和外星人后面重新绘制子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()

    # 让最近绘制的屏幕可见
    pygame.display.flip()


def update_bullets(bullets):
    """更新子弹的位置，并删除已消失的子弹"""
    bullets.update()

    # 删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def fire_bullet(ai_settings, screen, ship, bullets):
    """如果没有达到限制，就发射一颗子弹"""
    # 创建一颗子弹， 并将其加入到编组bullets中
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def fire_full_bullet(ai_settings, screen, ship, bullets):
    """加大火力"""
    # 创建一颗子弹， 并将其加入到编组bullets中
    i = 0
    while i < 80:
        # new_ship = ship.copy()
        # new_ship.rect.centerx = ship.rect.centerx
        ai_settings.ship_full_fire = True
        ai_settings.ship_full_fire_num = i * 2 + i

        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
        i += 1
