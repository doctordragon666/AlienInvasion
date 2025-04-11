# -*- coding:utf-8 -*-
# 日期：2021年11月20日19点04分
# 功能：
# 目的:
import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
import game_functions as gf


def run_game():
    """
    参数列表：初始配置，屏幕，状态，游戏按键，飞船，外星人， 子弹，记分牌
    """
    pygame.init()  # 屏幕初始化
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))  # 创建一个屏幕对象
    pygame.display.set_caption("A lien Invasion")  # 文件标题

    # 创建存储游戏统计信息的实例，并创建记分牌
    play_button = Button(ai_settings, screen, 'Play')
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    ship = Ship(ai_settings, screen)  # 创建一艘船
    bullets = Group()
    aliens = Group()

    gf.create_fleet(ai_settings, screen, ship, aliens)

    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, sb, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

if __name__ == '__main__':
    run_game()
