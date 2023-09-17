"""
File: game_functions.py
Contributor: Sean Burwen
Created: 9-7-2023
"""
import sys
import pygame


def check_events():
    """
    responds to keyboard & mouse input
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def update_screen(ai_settings, screen, ship):
    """
    update images on screen and flip to new screen
    """
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    pygame.display.flip()
