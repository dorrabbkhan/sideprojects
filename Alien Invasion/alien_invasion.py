import sys
import pygame
from settings import Settings

class AlienInvasion:
    """
    Class for the Alien Invasion game
    """

    def __init__(self):

        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        # initialize pygame, create a 1200x800 display

        pygame.display.set_caption("Alien Invasion")
        self.bg_color = (200, 200, 200)
        # set display caption and bg color

    def run_game(self):
        """
        Start the game
        """

        while True:
            
            self.screen.fill(self.settings.bg_color)
            # color the bg

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                    # exit if an input of exit is given
                    
            pygame.display.flip()
            # display most recent screen

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()