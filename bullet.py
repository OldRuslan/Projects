import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, g_settings, screen, ship):
        super().__init__()
        self.screen = screen
        self.g_settings = g_settings

        self.image = pygame.image.load('images/bullet.png')
        self.rect = self.image.get_rect()

        self.rect.centery = ship.rect.centery
        self.rect.left = ship.rect.right

    def update(self):
        self.rect.x += self.g_settings.bullet_speed_factor

    def blitme(self):
        self.screen.blit(self.image, self.rect)

