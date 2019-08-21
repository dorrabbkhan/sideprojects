class Settings:
    """
    Class to store settings for Alien Invasion game
    """

    def __init__(self):

        self.screen_width = 600
        self.screen_height = 600
        self.bg_color = (200, 200, 200)
        # set screen's resolution and bg color

        self.ship_limit = 3
        # set ship's speed and lives

        self.bullet_height = 20
        self.bullet_width = 5
        self.bullet_color = (100, 100, 100)
        self.bullets_allowed = 3
        # set settings for each bullet

        self.fleet_drop_speed = 10
        # set drop speed for aliens

        self.speedup_scale = 1.1
        # set how fast aliens speed up
        
        self.initialize_dynamic_settings()
        # initialize changing values

        self.score_scale = 1.5
        # set how fast score increases


    def initialize_dynamic_settings(self):
        """
        Initialize all values that will change throughout the game
        """

        self.alien_speed = 1.5
        self.bullet_speed = 1.5
        self.ship_speed = 2
        # set speeds of objects

        self.fleet_direction = 1
        # initialize fleet direction to right

        self.alien_points = 50
        # set points on killing an alien


    def increase_speed(self):
        """
        Increment speeds of objects
        """

        self.alien_points *= self.score_scale
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        # increment speeds