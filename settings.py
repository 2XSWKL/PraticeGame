import pygame


class Setting:
    """储存游戏中的所有设置项"""

    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 600
        self.screen_height = 900
        self.background_color = (0, 0, 0)
        # 飞船设置
        self.ship_speed = 10.0
