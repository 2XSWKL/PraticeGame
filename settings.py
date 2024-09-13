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
        self.fire_cd = 8
        self.ship_limit = 3
        # ⼦弹设置
        self.bullet_speed = 16.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (200, 200, 200)
        # 敌人设置
        self.enemy_count = 10
        self.enemy_speed = 4.0
        # 以什么速度加快游戏的节奏
        self.speedup_scale = 1.005
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化随游戏进⾏⽽变化的设置"""
        self.ship_speed = 10.0
        self.bullet_speed = 16.0
        self.enemy_speed = 4.0

    def increase_speed(self):
        """提⾼速度设置的值"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.enemy_speed *= self.speedup_scale
