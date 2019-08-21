"""
Class file for scoreboard to be used in Alien Invasion game
"""

import pygame.font


class Scoreboard:
    """
    Class for scoreboard in Alien Invasion game
    """

    def __init__(self, ai_game):

        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats
        # initialize screen, settings and stats

        self.text_color = (25, 25, 25)
        self.font = pygame.font.SysFont(None, 48)
        # set text color and font size

        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        # prep the score, level and high score images

    def prep_level(self):
        """
        Prep the level image for display
        """

        level = self.stats.level
        level_string = f'Level {level}'
        # obtain level and create string

        self.level_image = self.font.render(level_string, True, self.text_color, self.settings.bg_color)
        # render image

        self.level_rect = self.level_image.get_rect()
        self.level_rect.center = self.screen_rect.center
        self.level_rect.top = 20
        # get image rectangle and position it


    def prep_high_score(self):
        """
        Prep the high score image for display
        """

        high_score = int(round(self.stats.high_score, -1))
        # obtain high score rounded to nearest 10

        high_score_str = f'High score: {high_score:,}'
        self.high_score_image = self.font.render(
            high_score_str, True, self.text_color, self.settings.bg_color)
        # render high score

        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.left = self.screen_rect.left + 20
        self.high_score_rect.top = 20


    def prep_score(self):
        """
        Prep the score image for display
        """

        rounded_score = int(round(self.stats.score, -1))
        # obtain score rounded to nearest 10

        score_str = f"Score: {rounded_score:,}"
        # get the score

        self.score_image = self.font.render(
            score_str, True, self.text_color, self.settings.bg_color)
        # render the image

        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
        # get the score rect and position the score on the screen

    def show_score(self):
        """
        Display score on screen
        """

        self.screen.blit(self.level_image, self.level_rect)
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        # draw score

    def check_high_score(self):
        """
        Check for high score
        """

        if self.stats.score > self.stats.high_score:
            # if score is higher than the stored high score
            self.stats.high_score = self.stats.score
            self.prep_high_score()
            # set new high score and prep the high score image