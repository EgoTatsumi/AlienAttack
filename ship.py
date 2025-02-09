import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """Для управления кораблём"""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # загружает изображение корабля
        self.image = pygame.image.load(
            'other_files/spaceship.png')
        self.rect = self.image.get_rect()

        # каждый корабль появляется у нижнего края экрана
        self.rect.midbottom = self.screen_rect.midbottom
        self.moving_right = False
        self.moving_left = False

        # сохранение вещественной координаты корабля
        self.x = float(self.rect.x)

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        self.rect.x = self.x

    def blitme(self):
        """Рисует корабль в текущей позиции"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Размещает корабль в центре нижней стороны"""

        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
