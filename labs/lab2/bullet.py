"""
File: bullet.py
Contributor: Sean Burwen
Created: 9-17-2023
"""

import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """
    class to handle bullets from ship
    """
    def __init__(self, ai_settings, screen, ship):
        """
        Create bullet at ship's position
        """
        super(Bullet, self).__init__()
        self.screen = screen

        # Create bullet at 0,0 then set pos
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # store bullet pos as value
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """
        Move bullet up
        """
        # update decimal pos
        self.y -= self.speed_factor
        # update rect pos
        self.rect.y = self.y

    def draw_bullet(self):
        """
        Draw bullet to screen
        """
        pygame.draw.rect(self.screen, self.color, self.rect)
