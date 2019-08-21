"""
Main Python file for Alien Invasion game
"""

import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien


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
        # initialize pygame, settings and create a fullscreen display
        
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        # initialize ship, bullets and aliens

        self.settings.screen_height = self.screen.get_rect().height
        self.settings.screen_width = self.screen.get_rect().width
        # set width and height in settings

        pygame.display.set_caption("Alien Invasion")
        self.bg_color = (200, 200, 200)
        # set display caption and bg color


    def _create_fleet(self):
        """
        Create a fleet of aliens
        """

        alien = Alien(self)
        self.aliens.add(alien)
        # create alien and add to aliens

        alien_width, alien_height = alien.rect.size
        available_space_x = self.screen.get_rect().width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)
        # calculate the amount of space available for aliens and
        # then calculate the number of aliens to display

        ship_height = self.ship.rect.height
        available_space_y = self.screen.get_rect().height - ship_height - 6 * (alien_height)
        print(self.screen.get_rect().height, available_space_y, alien_height, ship_height)
        number_rows = available_space_y // (2* alien_height)
        print(number_rows)
        # calculate number of rows that fit on the screen

        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                # for each alien

                self._create_alien(alien_number, row_number)
            

    def _create_alien(self, alien_number, row_number):
        """
        Create alien based on alien number
        """

        alien = Alien(self)
        # create alien

        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.y = alien.rect.height + 2 * row_number * alien.rect.height
        alien.rect.y = alien.y
        # set its position based on alien number

        self.aliens.add(alien)
        # add to aliens group

    def run_game(self):
        """
        Start the game
        """

        while True:
            self._check_events()
            self._update_bullets()
            self._update_screen()
            self.ship.update()
            self.bullets.update()
            

            # check events that occured, update 
            # screen, bullets and ship accordingly


    def _update_bullets(self):
        """
        Update the bullets on the screen
        """

        self.bullets.update()
        # update bullets on screen

        for bullet in self.bullets.copy():
            if bullet.rect.bottom < 0:
                self.bullets.remove(bullet)
        # remove old bullets


    def _update_screen(self):
        """
        Update the screen
        """

        self.screen.fill(self.settings.bg_color)
        # color the bg

        self.ship.blitme()
        # draw the ship

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        # draw each bullet

        self.aliens.draw(self.screen)
        # draw the aliens

        pygame.display.flip()
        # display most recent screen


    def _fire_bullet(self):
        """
        Fire a bullet
        """

        if len(self.bullets) < self.settings.bullets_allowed:
        # if current number of bullets is less than what is allowed in settings

            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            # make new bullet and add to bullets group

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

        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
            # fire bullet if spacebar is pressed

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
