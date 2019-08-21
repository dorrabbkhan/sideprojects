"""
Main Python file for Alien Invasion game
"""

import sys
from time import sleep
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button


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
        self.stats = GameStats(self)
        # initialize pygame, settings, stats,
        # and create a fullscreen display

        self.play_button = Button(self, "Play")
        # initialize play button

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

    
    def _check_aliens_bottom(self):
        """
        Check if any alien has reached the bottom of the screen
        """

        screen_rect = self.screen.get_rect()
        # initialize screen's rectangle

        for alien in self.aliens.sprites():
        # for each alien

            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break
                # if alien crosses bottom of screen, call _ship_hit method


    def _ship_hit(self):
        """
        If shipt is hit by alien
        """

        if self.stats.ships_left > 0:
            # if any lives left

            self.stats.ships_left -= 1
            # decrement lives

        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

        self.bullets.empty()
        self.aliens.empty()
        # remove all bullets and aliens

        self._create_fleet()
        self.ship.center_ship()
        # create new fleet and center the ship

        sleep(0.5)
        # pause for half a second


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
        available_space_y = self.screen.get_rect().height - ship_height - \
            6 * (alien_height)
        number_rows = available_space_y // (2 * alien_height)
        # calculate number of rows that fit on the screen

        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                # for each alien

                self._create_alien(alien_number, row_number)
                # create alien

    def _check_fleet_edges(self):
        """
        Check if any edge has been hit
        """

        for alien in self.aliens.sprites():
            # for each alien
            if alien.check_edges():
                self._change_fleet_direction()
                break
                # if any alien has hit the edge, change fleet direction and break

    def _change_fleet_direction(self):
        """
        Change direction of fleet and drop the fleet
        """

        for alien in self.aliens.sprites():
            # for each alien

            alien.rect.y += self.settings.fleet_drop_speed
            # add drop speed's value to alien's y position to drop it downwards

        self.settings.fleet_direction *= -1
        # invert fleet's horizontal direction

    def _update_aliens(self):
        """
        Update the position of aliens
        """

        self._check_fleet_edges()
        self.aliens.update()
        # check if the fleet has hit the edge and update aliens

        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        # if there's any collision call this method

        self._check_aliens_bottom()
        # see if any alien hit bottom of screen


    def _create_alien(self, alien_number, row_number):
        """
        Create alien based on alien number
        """

        alien = Alien(self)
        # create alien

        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        # set its horizontal position based on alien number

        alien.y = alien_height + 2 * row_number * alien_height
        alien.rect.y = alien.y
        # set its vertical position based on row number

        self.aliens.add(alien)
        # add to aliens group

    def run_game(self):
        """
        Start the game
        """

        while True:
            self._check_events()

            if self.stats.game_active:

                self.ship.update()
                self._update_bullets()
                self._update_aliens()
                # do only if game is active

            self._update_screen()
            # check events that occured, update
            # screen, bullets, aliens and ship

    def _update_bullets(self):
        """
        Update the bullets on the screen
        """
        
        self.bullets.update()
        # update bullets on screen

        for bullet in self.bullets.copy():
            # for each bullet

            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        # remove old bullets if they're out of screen
        self.check_bullet_alien_collisions()

    def check_bullet_alien_collisions(self):
        """
        Check for collisions in bullets and aliens
        and respawn aliens of no more aliens are left
        """

        collisions = pygame.sprite.groupcollide(
        self.bullets, self.aliens, True, True)
        # check for collisions and remove bullet and alien on collision

        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
        # create new fleet if no more aliens



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

        if not self.stats.game_active:
            self.play_button.draw_button()
        # draw play button if game not active

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


    def _check_play_button(self, mouse_pos):
        """
        Check if play button was pressed and start game if it was
        """

        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        # check if button is pressed

        if button_clicked and not self.stats.game_active:
            # if button is pressed and game not active

            pygame.mouse.set_visible(False)
            # hide mouse
            
            self.stats.reset_stats()
            self.stats.game_active = True
            # reset stats and start game

            self.aliens.empty()
            self.bullets.empty()
            # empty all bullets and aliens

            self._create_fleet()
            self.ship.center_ship()
            # create fleet and center ship


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

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
    # run the game
