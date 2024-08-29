import pygame


class Settings:
    """储存游戏中的所有设置项"""

    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 600
        self.screen_height = 900
        self.background_color = (0, 0, 0)
        # 飞船设置
        self.ship_speed = 10.0
        self.fire_cd = 5
        # ⼦弹设置
        self.bullet_speed = 16.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (200, 200, 200)

