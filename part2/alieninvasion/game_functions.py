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
from alien import Alien


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

    if event.key == pygame.K_q:
        sys.exit()

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


def update_screen(ai_settings, screen, ship, aliens, bullets):
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
    # alien.blitme()
    aliens.draw(screen)

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


def create_fleet(ai_settings, screen, ship, aliens):
    """创建外星人舰队"""

    # 创建一个外星人 并计算一行容纳多少人外星人
    # 外星人间距为外星人宽度
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    number_aliens_x = get_number_aliens_x(ai_settings, alien_width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    # 创建一群外星人
    for number_row in range(number_rows):
        for alien_number in range(number_aliens_x):
            # 创建一个外星人并将其加入当前行
            create_alien(ai_settings, screen, aliens, alien_number, number_row)


def get_number_aliens_x(ai_settings, alien_width):
    """计算每行容纳多少外星人"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """创建一个外星人并将其放在当前行"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def get_number_rows(ai_settings, ship_height, alien_height):
    """计算屏幕可容纳多少行外星人"""
    # 屏幕高度 - 两处留白的位置 - 第一行外星人 - 飞船
    available_space_y = ai_settings.screen_height - (3 * alien_height) - ship_height
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows
