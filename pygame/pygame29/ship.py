import pygame
from settings import Settings

class Ship:
    """Клас для управління кораблем(головним героєм)"""

    def __init__(self, ai_game):
        """Ініціалізація корабля і задання його початкової позиції"""

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.settings = ai_game.settings

        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom
        self.moving_right = False
        self.moving_left = False
        self.moving_top = False
        self.moving_bottom = False
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        if self.moving_bottom and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed
        if self.moving_top and self.rect.top > Settings().screen_height:
            self.y -= self.settings.ship_speed
        
        self.rect.x = self.x
        self.rect.y = self.y

    def blit_me(self):
        """Малюємо корабель на поточній позиції"""

        self.screen.blit(self.image, self.rect)
