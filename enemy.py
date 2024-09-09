import pygame
from random import randint
from pygame.sprite import Sprite


class Enemy(Sprite):
    """管理敌人的类"""

    def __init__(self, ai_game):
        """初始化敌人并设定初始位置"""
        super().__init__()
        self.ai_game = ai_game
        self.settings = ai_game.settings
        self.screen = ai_game.screen
        # 加载敌人图像并加载 rect 属性
        self.image = pygame.image.load("images/enemy.bmp")
        self.rect = self.image.get_rect()
        # 设置外星人位置
        self.rect.x = randint(10, 590)
        self.rect.y = randint(0, 300)
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)
        # 飞船位置
        self.ship_x = ai_game.ship.x
        self.ship_y = ai_game.ship.y

    def update_ship_position(self, ai_game):
        """更新飞船位置"""
        self.ship_x = ai_game.ship.x
        self.ship_y = ai_game.ship.y

    def update(self):
        """更新敌人位置"""
        self.update_ship_position(self.ai_game)
        if self.x < self.ship_x:
            self.x += self.settings.enemy_speed
        else:
            self.x -= self.settings.enemy_speed
        if self.y < self.ship_y:
            self.y += self.settings.enemy_speed
        else:
            self.y -= self.settings.enemy_speed
        self.rect.x = self.x
        self.rect.y = self.y
