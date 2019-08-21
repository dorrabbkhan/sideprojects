"""
Class file for alien in alien invasion game
"""

import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """
    Alien class for alien invasion game
    """

    def __init__(self, ai_game):

        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        # initialize screen and settings

        self.image = pygame.image.load('img/alien.bmp')
        self.image = pygame.transform.rotozoom(self.image, 0, 0.1)
        self.rect = self.image.get_rect()
        # load the image of alien and get its rect

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # place alien to the top left

        self.x = float(self.rect.x)
        # set x as a decimal value

    def update(self):
        """
        Update alien's position
        """

        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x
        # add alien_speed to alien's position in the direction of fleet_direction

    def check_edges(self):
        """
        Check if an alien has hit the edge
        """

        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.x < 0:
            return True
        return False
        # check if edge has been hit
