import pygame.font


class Scoreboard:
    """显示信息得分的类"""

    def __init__(self, ai_game):
        """初始化显示得分属性的类"""
        self.score_rect = None
        self.score_image = None
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats
        # 显⽰得分信息时使⽤的字体设置
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        # 准备初始得分图像
        self.prep_score()

    def prep_score(self):
        """将得分渲染为图像"""
        score_str = str(self.stats.score)
        self.score_image = self.font.render(
            score_str, True, self.text_color, self.settings.background_color)
        # 在屏幕右上⾓显⽰得分
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """在屏幕上显⽰得分"""
        self.screen.blit(self.score_image, self.score_rect)
