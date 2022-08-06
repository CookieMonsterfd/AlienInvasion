#Перед запуском програми встановіть pygame у командному рядку за допомогою pip3 install pygame

import pygame
import sys
from ship import Ship
from settings import Settings

class Alien_Invasion:
    """Загальний клас для управління грою"""

    def __init__(self):
        """Ініціалізує(створює) гру та її ресурси"""

        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        pygame.display.set_caption(self.settings.game_caption)
        self.ship = Ship(self)
        self.bg_color = self.settings.bg_color

    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
            
            pygame.display.flip()

    def _check_events(self):
        """Відповідає на взаємодію з мишкою та клавіатурою"""

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)

    
    def _check_keydown_events(self,event):
        """Відповідає за натискання клавіш"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            self.ship.moving_top = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_bottom = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self,event):
        """Відповідає за відтискання клавіш"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_top = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_bottom = False

    def _update_screen(self):
        self.screen.fill(self.bg_color)
        self.ship.blit_me()

if __name__ == "__main__":
    ai = Alien_Invasion()
    ai.run_game()
