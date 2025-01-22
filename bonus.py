import pygame
from random import randint
from pygame.sprite import Sprite


class Bonus(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.img = pygame.image.load("other_files/bonus.png")
        self.rect = self.img.get_rect()
        self.y = float(self.rect.y)
        self.rect.midtop = (randint(0, 1900), 0)


    def update(self):
        """Перемещает бонус вниз по экрану"""
        self.y += self.settings.bonus_speed
        self.rect.y = self.y

    def blitme(self):
        """Рисует бонус в текущей позиции"""
        self.screen.blit(self.img, self.rect)
