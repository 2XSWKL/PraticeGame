import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """管理飞船发射的子弹"""
    def __init__(self, ai_game):
        """创建子弹"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
        self.rect = pygame.Rect(
            ai_game.ship.x + 6, ai_game.ship.y,
            self.settings.bullet_width, self.settings.bullet_height)
        self.y = float(self.rect.y)

    def update(self):
        """"移动子弹"""
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        """绘制子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)

