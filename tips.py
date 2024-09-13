import pygame.font


class Tips:
    """为游戏创建提示的类"""
    def __init__(self, ai_game, msg, bg):
        """初始化按钮的属性"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        # 设置按钮的尺⼨和其他属性
        self.width, self.height = 200, 50
        self.button_color = bg
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        # 创建按钮的 rect 对象，并使其居中
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        # 按钮的标签只需创建⼀次
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """将 msg 渲染为图像，并使其在提示上居中"""
        self.msg_image = self.font.render(
            msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
        self.msg_image_rect.y += 60

    def draw_tips(self):
        """绘制⼀个⽤颜⾊填充的提示，再绘制⽂本"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)