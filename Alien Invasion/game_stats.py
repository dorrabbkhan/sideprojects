"""
Class file for game statistics in Alien Invasion
"""

class GameStats:
    """
    Class for statistics in the Alien Invasion game
    """

    def __init__(self, ai_game):
        
        self.settings = ai_game.settings
        self.reset_stats()
        self.high_score = 0
        self.game_active = False
        # initialize settings and reset all stats
        # start game as inactive


    def reset_stats(self):
        """
        Initialize all statistics
        """

        self.score = 0
        self.level = 1
        # initialize score, level

        self.ships_left = self.settings.ship_limit
        # set ship's lives to its setting