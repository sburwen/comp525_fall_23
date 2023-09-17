"""
File: ship.py
Contributor: Sean Burwen
Created: 9-7-2023
"""
import pygame


class Ship:
    """
    Creates the ship.
    """
    def __init__(self, screen):
        """
        Initialize ship and set starting position.
        """
        self.screen = screen

        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """
        Draw ship at current location.
        """
        self.screen.blit(self.image, self.rect)
