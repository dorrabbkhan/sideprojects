"""
Class file for button in Alien Invasion game
"""
import pygame.font


class Button:
    """
    Class for button in Alien Invasion game
    """

    def __init__(self, ai_game, msg):

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        # initialize screen

        self.width, self.height = 500, 200
        self.button_color = (100, 100, 100)
        self.text_color = (240, 240, 240)
        self.font = pygame.font.SysFont(None, 48)
        # set the styling for the button and text

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        # create button and position it

        self._prep_msg(msg)
        # add message to it

    def _prep_msg(self, msg):
        """
        Render text as image and add to button
        """

        self.msg_image = self.font.render(
            msg, True, self.text_color, self.button_color)
        # render the msg text

        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
        # get the text's rect and position it to center of button

    def draw_button(self):
        """
        Draw button on screen
        """

        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
        # draw button on screen
