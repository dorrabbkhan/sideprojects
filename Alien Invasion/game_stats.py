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
        self.game_active = True
        # initialize settings, game_active flag and reset all stats

    def reset_stats(self):
        """
        Initialize all statistics
        """

        self.ships_left = self.settings.ship_limit
        # set ship's lives to its setting