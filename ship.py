import pygame


class Ship:
    """管理飞船的类"""

    def __init__(self, ai_game):
        """初始化飞船"""
        # 位置,大小,图像
        self.screen = ai_game.screen
        self.setting = ai_game.setting
        self.screen_rect = ai_game.screen.get_rect()
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        # 移动标志
        self.displacement_x = 0.0
        self.displacement_y = 0.0
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def move_x(self):
        if (
                self.moving_right and abs(self.displacement_x) < self.setting.ship_speed
                and self.rect.right < self.screen_rect.right
                ):
            self.displacement_x += 0.4
        if (
                self.moving_left and abs(self.displacement_x) < self.setting.ship_speed
                and self.rect.left > self.screen_rect.left
                ):
            self.displacement_x -= 0.4

        if self.displacement_x == 0.0:
            pass
        elif self.displacement_x > 0.0:
            self.displacement_x -= 0.2
        elif self.displacement_x < 0.0:
            self.displacement_x += 0.2
        return self.displacement_x

    def move_y(self):
        if (
                self.moving_down and abs(self.displacement_y) < self.setting.ship_speed
                and self.rect.bottom < self.screen_rect.bottom
                ):
            self.displacement_y += 0.4
        if (
                self.moving_up and abs(self.displacement_y) < self.setting.ship_speed
                and self.rect.top > self.screen_rect.top
                ):
            self.displacement_y -= 0.4

        if self.displacement_y == 0.0:
            pass
        elif self.displacement_y > 0.0:
            self.displacement_y -= 0.2
        elif self.displacement_y < 0.0:
            self.displacement_y += 0.2
        return self.displacement_y

    def update(self):
        if self.move_x():
            self.x += self.move_x()
        if self.move_y():
            self.y += self.move_y()
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """绘制飞船"""
        self.screen.blit(self.image, self.rect)
