"""
File: alien.py
Contributor: Sean Burwen
Created: 9-28-2023
"""
import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """
    class represents single alien
    """

    def __init__(self, ai_settings, screen):
        """
        initialize alien and set starting pos
        """
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # load alien img
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # start new alien near top left of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store alien pos
        self.x = float(self.rect.x)

    def blitme(self):
        """
        draw alien at current pos
        """
        self.screen.blit(self.image, self.rect)
