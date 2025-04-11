# -*- coding:utf-8 -*-
# 日期：2021年11月21日
# 功能：
# 目的：
class GameStats:
    """跟踪游戏统计信息"""
    def __init__(self, ai_settings):
        """
        参数要求：设置
        """
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False
        self.high_score = 0

    def reset_stats(self):
        """
        重置游戏状态
        """
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1

# 在python中运行的结果是：
# 总结：
