import pygame
from random import randint
from pygame.sprite import Sprite

class Enemy(Sprite):
    def __init__(self, g_settings, screen):
        super().__init__()
        self.screen = screen
        self.g_settings = g_settings

        # загрузка изображения корабля противника
        self.image = pygame.image.load('images/enemy.png')
        self.rect = self.image.get_rect()
        self.screen.rect = screen.get_rect()

        # позиционирование новых астероидов на экране
        self.bias = randint(-360, 360)
        self.rect.centery = self.screen_rect.centery + self.bias
        self.rect.right = self.screen_rect.right

    def update(self):
        self.x = float(self.rect.x)
        self.x -= self.g_settings.asteroid_speed
        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)