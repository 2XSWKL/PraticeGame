import pygame


class GameStats:
    """统计游戏信息"""
    def __init__(self, ai_game):
        self.score = None
        self.ships_left = None
        self.settings = ai_game.settings
        self.reset_stats()

    def reset_stats(self):
        """初始化在游戏运⾏期间可能变化的统计信息"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
