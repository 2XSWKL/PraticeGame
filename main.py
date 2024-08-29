import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet


class AircraftInvasion:
    """"管理游戏资源和行为的类"""

    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()
        pygame.display.set_caption("AircraftInvasion")
        self.settings = Settings()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

    def _check_events(self):
        """响应事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # 关闭游戏
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_k_down(event)
            elif event.type == pygame.KEYUP:
                self._check_k_up(event)

    def _check_k_down(self, event):
        if event.key == pygame.K_ESCAPE:
            sys.exit()
        elif event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            self.ship.fired = True

    def _check_k_up(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False
        elif event.key == pygame.K_SPACE:
            self.ship.fired = False

    def _update_screen(self):
        """更新屏幕"""
        # 重绘屏幕
        self.screen.fill(self.settings.background_color)
        # 刷新屏幕
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()

        pygame.display.flip()

    def _fire_bullet(self):
        """创建子弹，并将其加入编组bullets"""
        if self.ship.fire_cd > 0:
            self.ship.fire_cd -= 1
        if self.ship.fired and self.ship.fire_cd <= 0:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            self.ship.fire_cd = self.settings.fire_cd

    def _update_bullet(self):
        """更新子弹"""
        # 更新子弹位置
        self.bullets.update()
        # 尝试开火
        self._fire_bullet()
        # 删除子弹
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def run_game(self):
        """创建游戏循环"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullet()
            self._update_screen()
            self.clock.tick(60)


if __name__ == '__main__':
    # 创建游戏实例并运行游戏
    ai = AircraftInvasion()
    ai.run_game()

