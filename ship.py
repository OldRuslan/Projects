import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self, g_settings, screen):
        super().__init__()
        """Инициализирует корабль и задает его начальную позицию."""
        self.screen = screen
        self.g_settings = g_settings

        #загрузка изображения корабля и получение прямоугольника
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #каждый новый корабль появляется у левого края экрана
        self.rect.centery = self.screen_rect.centery
        self.rect.left = self.screen_rect.left

        #Флаг перемещения
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Обновляет позицию корабля с учетом флага"""

        #Обновляется атрибут center а не rect
        if self.moving_up and self.rect.top > 0:
            self.rect.centery -= self.g_settings.ship_speed
        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery += self.g_settings.ship_speed

    def blitme(self):
        """Рисует корабль в текущей позиции"""
        self.screen.blit(self.image, self.rect)
