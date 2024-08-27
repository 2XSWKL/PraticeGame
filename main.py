import sys
import time

import pygame
from settings import Setting
from ship import Ship


class AircraftInvasion:
    """"管理游戏资源和行为的类"""

    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()
        pygame.display.set_caption("AircraftInvasion")
        self.setting = Setting()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(
            (self.setting.screen_width, self.setting.screen_height))
        self.ship = Ship(self)

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
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_ESCAPE:
            sys.exit()

    def _check_k_up(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _update_screen(self):
        """更新屏幕"""
        # 重绘屏幕
        self.screen.fill(self.setting.background_color)
        self.ship.blitme()
        # 刷新屏幕
        pygame.display.flip()

    def run_game(self):
        """创建游戏循环"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
            self.clock.tick(60)


if __name__ == '__main__':
    # 创建游戏实例并运行游戏
    ai = AircraftInvasion()
    ai.run_game()
