import pygame
from pygame.sprite import Sprite
from random import randint

class Asteroids(Sprite):
    def __init__(self, g_settings, screen):
        super().__init__()
        self.g_settings = g_settings
        self.screen = screen

        # загрузка изображения астероида и получение прямоугольника
        self.image = pygame.image.load('images/aestroid_brown.png')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

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