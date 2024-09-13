import sys
import pygame
from time import sleep
from settings import Settings
from ship import Ship
from bullet import Bullet
from enemy import Enemy
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
from tips import Tips


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
        self.stats = GameStats(self)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.enemys = pygame.sprite.Group()
        # 游戏启动后处于活动状态
        self.game_active = False
        # 创建存储游戏统计信息的实例，并创建记分牌
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)
        # 创建 Play 按钮
        self.play_button = Button(self, "Play")
        # 显示提示信息
        self.wlc_tip = Tips(self, "udlr-move SPACE-shot Esc-quit", (0, 0, 0))

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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

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
        # 检查是否有⼦弹击中了敌⼈
        # 如果是，就删除相应的⼦弹和敌人
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.enemys, True, True)
        if collisions:
            self.settings.increase_speed()
            for enemy in collisions.values():
                self.stats.score += len(enemy)
            self.sb.prep_score()

    def _create_fleet(self):
        """创建一个敌人舰队"""
        while len(self.enemys) < self.settings.enemy_count:
            new_enemy = Enemy(self)
            self.enemys.add(new_enemy)

    def _check_enemy_ship_collision(self):
        """检测飞船与敌人的碰撞"""
        if pygame.sprite.spritecollideany(self.ship, self.enemys):
            self._ship_hit()

    def _ship_hit(self):
        """响应⻜船和外星⼈的碰撞"""
        if self.stats.ships_left > 0:
            # 将 ships_left 减 1
            self.stats.ships_left -= 1
            # 清空外星⼈列表和⼦弹列表
            self.bullets.empty()
            self.enemys.empty()
            # 创建⼀个新的外星舰队，并将⻜船放在屏幕底部的中
            self._create_fleet()
            self.ship.center_ship()
            # 暂停
            sleep(0.5)
        else:
            # 清空外星⼈列表和⼦弹列表
            self.bullets.empty()
            self.enemys.empty()
            self.ship.center_ship()
            # 停止游戏
            self.game_active = False
            pygame.mouse.set_visible(True)

    def _check_play_button(self, mouse_pos):
        """在玩家单击 Play 按钮时开始新游戏"""
        if self.play_button.rect.collidepoint(mouse_pos):
            # 重置游戏的统计信息
            self.stats.reset_stats()
            self.game_active = True
            self.sb.prep_score()
            # 清空外星⼈列表和⼦弹列表
            self.bullets.empty()
            self.enemys.empty()
            # 创建⼀个新的外星舰队，并将⻜船放在屏幕底部的中央
            self._create_fleet()
            self.ship.center_ship()
            # 隐藏光标
            pygame.mouse.set_visible(False)
            # 还原游戏设置
            self.settings.initialize_dynamic_settings()

    def _update_screen(self):
        """更新屏幕"""
        # 重绘屏幕
        self.screen.fill(self.settings.background_color)
        # 刷新屏幕
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.enemys.draw(self.screen)
        # 显⽰得分
        self.sb.show_score()
        # 如果游戏处于⾮活动状态，就绘制 Play 按钮
        if not self.game_active:
            self.wlc_tip.draw_tips()
            self.play_button.draw_button()

        pygame.display.flip()

    def run_game(self):
        """创建游戏循环"""
        while True:
            self._check_events()
            if self.game_active:
                self.ship.update()
                self.enemys.update()
                self._create_fleet()
                self._update_bullet()
                self._check_enemy_ship_collision()
            self._update_screen()
            self.clock.tick(60)


if __name__ == '__main__':
    # 创建游戏实例并运行游戏
    ai = AircraftInvasion()
    ai.run_game()
