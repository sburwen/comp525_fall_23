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
    def __init__(self, ai_settings, screen):
        """
        Initialize ship and set starting position.
        """
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)

        # movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """
        Update ship position via movement flag.
        """
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center

    def blitme(self):
        """
        Draw ship at current location.
        """
        self.screen.blit(self.image, self.rect)
