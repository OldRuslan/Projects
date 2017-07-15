import sys
import pygame
from bullet import Bullet
from asteroids import Asteroids

def check_keydown_events(event, g_settings, screen, ship, bullets):
    """Реагирует на нажатие клавиш"""
    if event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(g_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event, ship):
    """Реагирует на отпускание клавиш"""
    if event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False

def check_events(g_settings, screen, ship, bullets):
    """Обрабатывает нажатие клавиш и события мыши"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, g_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def fire_bullet(g_settings, screen, ship, bullets):
    """Выпускает пулю если максимум еще не достигнут"""

    # создание новой пули и включение ее в группу bullets
    if len(bullets) < g_settings.bullets_allowed:
        new_bullet = Bullet(g_settings, screen, ship)
        bullets.add(new_bullet)

def update_bullets(g_settings, asteroids, bullets, ship):
    """Обновляет позиции пуль и уничтожает старые пули"""

    #обновление позиций
    bullets.update()

    #удаление пуль вышедших за край экрана
    for bullet in bullets.copy():
        if bullet.rect.left > g_settings.screen_width:
            bullets.remove(bullet)

    objects_collide(bullets, asteroids, ship)

def create_asteroid(g_settings, screen, asteroids):
    if len(asteroids) < 1:
        asteroid = Asteroids(g_settings, screen)
        asteroids.add(asteroid)

def update_asteroid(g_settings, screen, asteroids, bullets, ship):
    create_asteroid(g_settings, screen, asteroids)
    screen_rect = screen.get_rect()

    asteroids.update()

    for ast in asteroids.copy():
        if ast.rect.left < screen_rect.centerx and len(asteroids) < 2:
            asteroid = Asteroids(g_settings, screen)
            asteroids.add(asteroid)
        elif ast.rect.right < screen_rect.left:
            asteroids.remove(ast)

def objects_collide(bullets, asteroids, ship):
    ship_collide = pygame.sprite.groupcollide(ship, asteroids, True, True)
    collide_bullet = pygame.sprite.groupcollide(bullets, asteroids, True, True)

def update_screen(g_settings, screen, ship, bullets, asteroids, bg_image):
    """Обновляет изображение на экаране и отображает новый экран"""

    # при каждом проходе цикла перерисовывается экран
    screen.fill(g_settings.bg_color)
    screen.blit(bg_image, (0,0))

    for s in ship.sprites():
        s.blitme()

    for ast in asteroids.sprites():
        ast.blitme()

    if ship:
        for bullet in bullets.sprites():
            bullet.blitme()

    # отображение последнего прорисованного экрана
    pygame.display.flip()