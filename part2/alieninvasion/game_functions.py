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
from random import randint
from time import sleep


def check_event(ai_settings, screen, stats, sb, play_button, ship, bullets, aliens):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # 鼠标事件
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y)

        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event, ai_settings, screen, stats, sb, ship, bullets, aliens)
        elif event.type == pygame.KEYUP:
            check_keyup_event(event, ship)


def check_keydown_event(event, ai_settings, screen, stats, sb, ship, bullets, aliens):
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
    if event.key == pygame.K_p:
        start_game(ai_settings, screen, stats, sb, ship, bullets, aliens)


def check_keyup_event(event, ship):
    """键盘松开"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_play_button(ai_settings, screen, stats, sb, play_button, ship, bullets, aliens, mouse_x, mouse_y):
    """玩家单机play按钮时开始游戏"""
    button_click = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_click and not stats.game_active:
        start_game(ai_settings, screen, stats, sb, ship, bullets, aliens)


def update_screen(ai_settings, stats, sb, screen, ship, aliens, bullets, play_button):
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

    # 显示得分
    sb.show_score()

    # 如果游戏处于非活动状态，就绘制Play按钮
    if not stats.game_active:
        play_button.draw_button()

    # 让最近绘制的屏幕可见
    pygame.display.flip()


def update_bullets(ai_settings, stats, sb, screen, ship, bullets, aliens):
    """更新子弹的位置，并删除已消失的子弹"""
    bullets.update()

    # 删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    # 检查是否有子弹击中外星人 如果是这样的 删除相应的子弹和外星人
    check_bulled_alien_collisions(ai_settings, stats, sb, screen, ship, bullets, aliens)


def check_bulled_alien_collisions(ai_settings, stats, sb, screen, ship, bullets, aliens):
    # 检查是否有子弹击中外星人 如果是这样的 删除相应的子弹和外星人
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()
        check_high_score(stats, sb)

    if len(aliens) == 0:
        # 删除现有的子弹并新建一群外星人
        bullets.empty()
        # 提速
        ai_settings.increase_speed()
        # 提高等级
        stats.level += 1
        sb.prep_level()

        create_fleet(ai_settings, screen, ship, aliens)


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
        ai_settings.bullet_speed_factor = 10
        ai_settings.bullet_width = 5
        ai_settings.bullet_height = 15
        ai_settings.bullet_color = 0, 0, 255

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
            # 随机创建
            random_number = randint(0, 10)
            if alien_number == random_number or number_row == random_number:
                continue
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


def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
    """
    检查是否有外星人位于屏幕边缘
    更新外星人群中的所有外星人位置
    """
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # 检测外形人和飞船之间碰撞
    if pygame.sprite.spritecollideany(ship, aliens):
        print("--------------- ship hit!!! ------------------")
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)

    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)


def check_fleet_edges(ai_settings, aliens):
    """有外星人到达边缘时采取相应的措施"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    """将外星人下移并改变方向"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    """响应被外星人撞到的飞船"""
    if stats.ships_left > 0:
        # 将ships_left减1
        stats.ships_left -= 1

        # 清空外星人列表和子弹
        aliens.empty()
        bullets.empty()

        # 创建一群新的外星人 并将飞船放到屏幕底端中央
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        # 暂停
        sleep(1)
    else:
        # game over
        stats.game_active = False
        # 显示光标
        pygame.mouse.set_visible(True)


def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    """检查是否有外星人到达屏幕底端"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            """像飞船撞击一样处理"""
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)


def start_game(ai_settings, screen, stats, sb, ship, bullets, aliens):
    """ 开始游戏 """

    # 重置游戏设置
    ai_settings.initialize_dynamic_settings()

    # 隐藏光标
    pygame.mouse.set_visible(False)

    # 重置游戏统计信息
    stats.reset_stats()
    stats.game_active = True

    # 重新记分牌图像
    sb.prep_score()
    sb.prep_high_score()
    sb.prep_level()

    # 清空外星人 子弹
    aliens.empty()
    bullets.empty()

    # 创建一群新的外星人 飞船居中
    create_fleet(ai_settings, screen, ship, aliens)
    ship.center_ship()


def check_high_score(stats, sb):
    """检查是否诞生了新的最高分"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()