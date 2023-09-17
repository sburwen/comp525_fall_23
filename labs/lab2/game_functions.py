"""
File: game_functions.py
Contributor: Sean Burwen
Created: 9-7-2023
"""
import sys
import pygame


def check_keydown_events(event, ship):
    """
    responds to keypress
    """
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True


def check_keyup_events(event, ship):
    """
    responds to key release
    """
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ship):
    """
    responds to keyboard & mouse input
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship):
    """
    update images on screen and flip to new screen
    """
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    pygame.display.flip()
