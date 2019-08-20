class Settings:
    """
    Class to store settings for Alien Invasion game
    """

    def __init__(self):

        self.screen_width = 600
        self.screen_height = 600
        self.bg_color = (200, 200, 200)
        # set screen's resolution and bg color

        self.ship_speed = 1.5
        # set ship's speed

        self.bullet_speed = 1.0
        self.bullet_height = 20
        self.bullet_width = 5
        self.bullet_color = (100, 100, 100)
        # set settings for each bullet
