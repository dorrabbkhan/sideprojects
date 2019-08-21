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
        # initialize screen

        self.image = pygame.image.load('img/alien.bmp')
        self.image = pygame.transform.rotozoom(self.image, 0, 0.1)
        self.rect = self.image.get_rect()
        # load the image of alien and get its rect

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # place alien to the top left

        self.x = float(self.rect.x)
        # set x as a decimal value
        