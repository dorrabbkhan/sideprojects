"""
Main Python file for Alien Invasion game
"""

import sys
import pygame
from settings import Settings
from ship import Ship


class AlienInvasion:
    """
    Class for the Alien Invasion game
    """

    def __init__(self):
        """
        Initialize the AlienInvasion game
        """

        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.ship = Ship(self)
        # initialize pygame, ship, settings and create a fullscreen display

        self.settings.screen_height = self.screen.get_rect().height
        self.settings.screen_width = self.screen.get_rect().width
        # set width and height in settings

        pygame.display.set_caption("Alien Invasion")
        self.bg_color = (200, 200, 200)
        # set display caption and bg color

    def run_game(self):
        """
        Start the game
        """

        while True:
            self._check_events()
            self._update_screen()
            self.ship.update()
            # check events that occured, update screen and ship accordingly

    def _update_screen(self):
        """
        Update the screen
        """

        self.screen.fill(self.settings.bg_color)
        # color the bg

        self.ship.blitme()
        # draw the ship

        pygame.display.flip()
        # display most recent screen

    def _check_keyup_events(self, event):
        """
        Check events that occured on keyup
        """

        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
            # set moving_right flag to False if right key is lifted

        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
            # set moving_left flag to False if left key is lifted

    def _check_keydown_events(self, event):
        """
        Check events that occured on keydown
        """

        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
            # set moving_right flag to True if left key is pressed

        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
            # set moving_left flag to True if left key is pressed

        elif event.key == pygame.K_q:
            sys.exit()
            # quit if Q is pressed

    def _check_events(self):
        """
        Listen to events
        """

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                # exit if window is closed

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
                # check keydown events if a key is pressed

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
                # check keyup events if a key is lifted


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
    # run the game
