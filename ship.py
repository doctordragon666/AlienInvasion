# -*- coding:utf-8 -*-
# 日期：
# 功能：船
# 目的：
import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    def __init__(self, ai_settings, screen):
        """初始化飞船并设置其初始位置"""
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load('images/naruto.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # 将每艘新飞创放在屏幕底部中间
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # 移动标志
        self.moving_right = False
        self.moving_left = False
        # 在飞船的属性center中存储小数
        self.center = float(self.rect.centerx)

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """更新飞船"""
        # 根据移动标志调整飞船位置
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        # 如果飞船外接矩形的右边缘的x坐标加移动坐标大于屏幕的右边缘，则停止运行
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.center -= self.ai_settings.ship_speed_factor
        # 根据self.center更新rect对象
        self.rect.centerx = self.center

    def center_ship(self):
        """把船放回游戏屏幕中间"""
        self.center = self.screen_rect.centerx

# 在python中运行的结果是：
# 总结：
