# -*- coding:utf-8 -*-
# 日期：2021年11月21日10点20分
# 功能：
# 目的：
import pygame


class Settings:
    """存储所有的设置类"""
    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 1080
        self.screen_height = 600
        self.bg_color = (212, 218, 240)
        # 飞船的设置
        self.ship_limit = 3
        # 子弹的设置
        self.image = pygame.image.load("images/luoxuanwan.bmp")
        self.bullet_width = self.image.get_width()
        self.bullet_height = self.image.get_height()
        self.bullets_allowed = 50
        # 外星人的设置
        self.fleet_drop_speed = 50
        # 以什么样的速度加快游戏节奏
        self.speedup_scale = 1.5
        self.score_scale = 990
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1
        self.bullet_speed_factor = 5
        self.alien_speed_factor = 0.1
        # 为1时表示左移，为-1表示右移
        self.fleet_direction = 1
        # 记分
        self.alien_points = 50

    def increase_speed(self):
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.ship_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points*self.score_scale)