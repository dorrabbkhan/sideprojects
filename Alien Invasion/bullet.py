"""
Class file for bullet in Alien Invasion game
"""

import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """
    Bullet class for Alien Invasion
    """

    def __init__(self, ai_game):
        """
        Make bullet at current position of ship
        """

        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
        # initialize screen, settings and color of bullet

        self.rect = pygame.Rect(
            0, 0, self.settings.bullet_width, self.settings.bullet_height)
        # initialize the bullet with the set width and height

        self.rect.midtop = ai_game.ship.rect.midtop
        self.y = float(self.rect.y)
        # set its position and obtain decimal version of its vertical position

    def update(self):
        """
        Update bullet's position
        """

        self.y -= self.settings.bullet_speed
        self.rect.y = self.y
        # make the bullet move forward

    def draw_bullet(self):
        """
        Draw the bullet on the screen
        """

        pygame.draw.rect(self.screen, self.color, self.rect)
        # draw the bullet
