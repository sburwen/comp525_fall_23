"""
File: alien_invasion.py
Contributor: Sean Burwen
Created: 9-7-2023
"""
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    """
    runs the game.
    """
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(screen)

    while True:
        gf.check_events()
        gf.update_screen(ai_settings, screen, ship)


run_game()
