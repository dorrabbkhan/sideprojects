import sys
import pygame

class AlienInvasion:
    """
    Class for the Alien Invasion game
    """

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """
        Start the game
        """

        while True:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                    # exit if an input of exit is given
                    
            pygame.display.flip()
            # display most recent screen

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()