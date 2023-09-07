"""
File: alien_invasion.py
Contributor: Sean Burwen
Created: 9-7-2023
"""

import sys
import pygame


def run_game():
    """
    runs game
    """
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.flip()


run_game()
