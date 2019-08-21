"""
Python class file for ship to be used in Alien Invasion game
"""

import pygame
from settings import Settings

class Ship:
    """
    Class for the ship in Alien Invasion
    """

    def __init__(self, ai_game):
        """
        Initialize the ship
        """

        self.settings = Settings()
        self.screen =  ai_game.screen
        # initialize settings and screen

        self.image = pygame.image.load('img/ship.bmp')
        self.image = pygame.transform.rotozoom(self.image, 0, 0.1)
        # load and transform image of ship

        self.screen_rect = ai_game.screen.get_rect()
        self.rect = self.image.get_rect()
        # get rectangles for screen and ship

        self.rect.midbottom = self.screen_rect.midbottom
        # set ship at midbottom of the screen

        self.moving_right = False
        self.moving_left = False
        # initialize moving flags to False initially

        self.x = float(self.rect.x)
        # initialize float version of x position

    def blitme(self):
        """
        Draw the ship
        """

        self.screen.blit(self.image, self.rect)

    def update(self):
        """
        Update ship's position
        """

        if self.moving_left and self.rect.x > 0:
            self.x -= self.settings.ship_speed
            # decrement x position if moving_left
            # is true and ship is not at the left edge

        elif self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
            # increment x position if moving_right
            # is true and ship is not at the right edge

        self.rect.x = self.x
        # update ship's position


    def center_ship(self):
        """
        Center ship's position
        """

        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        # recenter ship and put new x value into self.x