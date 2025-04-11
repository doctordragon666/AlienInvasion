# -*- coding:utf-8 -*-
# 日期：
# 功能：
# 目的：
import pygame.font


class Button:
    """按钮类"""
    def __init__(self, ai_settings, screen, msg):
        """
        参数要求：设置，屏幕，和信息（按钮的字）
        """
        # 初始化按钮的属性
        self.screen = screen
        self.screen_rect = screen.get_rect()
        # 设置按钮的其他属性
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont("arial", 48)
        # 创建按钮的对象，并居中
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        # 按钮的标签只需创建一次
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """贴上信息"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """画按钮"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

# 在python中运行的结果是：
# 总结：
