import pygame
import functions
from ship import Ship
from settings import Settings
from pygame.sprite import Group, GroupSingle

def start_game():
    pygame.init()
    fpsClock = pygame.time.Clock()
    g_settings = Settings()
    screen = pygame.display.set_mode((g_settings.screen_width, g_settings.screen_height))
    bg_image = g_settings.bg_image.convert()
    pygame.display.set_caption('Space Battle')


    player = Ship(g_settings, screen)
    ship = GroupSingle(player)
    bullets = Group()
    asteroids = Group()

    while True:
        ship.update()
        functions.check_events(g_settings, screen, player, bullets)
        functions.update_bullets(g_settings, asteroids, bullets, ship)
        functions.update_asteroid(g_settings, screen, asteroids, bullets, ship)
        functions.update_screen(g_settings, screen, ship, bullets, asteroids, bg_image)

start_game()