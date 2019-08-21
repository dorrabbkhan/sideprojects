class Settings:
    """
    Class to store settings for Alien Invasion game
    """

    def __init__(self):

        self.screen_width = 600
        self.screen_height = 600
        self.bg_color = (200, 200, 200)
        # set screen's resolution and bg color

        self.ship_speed = 2
        self.ship_limit = 3
        # set ship's speed and lives

        self.bullet_speed = 1.5
        self.bullet_height = 20
        self.bullet_width = 5
        self.bullet_color = (100, 100, 100)
        self.bullets_allowed = 3
        # set settings for each bullet

        self.alien_speed = 1.5
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
        # set settings for aliens
