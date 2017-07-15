import pygame

class Settings():
    """Класс для хранения всех настрое игры"""

    def __init__(self):
        """инициализирует настройки игры."""

        #параметры экрана
        self.screen_width = 1366
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # фоновое изображение
        self.bg_image = pygame.image.load('images/back_3.png')

        #параметры корабля
        self.ship_speed = 3

        #параметры пуль
        self.bullet_speed_factor = 3
        self.bullets_allowed = 5

        #параметры астероидов
        self.asteroid_speed = 3.5