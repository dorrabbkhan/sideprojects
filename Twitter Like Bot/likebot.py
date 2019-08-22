"""
Python script to automatically like tweets that contain
a specific hashtag. Made with selenium and geckodriver
"""

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class LikeBot:
    """
    Class for twitter hashtag liking bot
    """

    def __init__(self, username, password):

        self.username = username
        self.password = password
        # initialize username and password

        self.browser = webdriver.Firefox()

    def login(self):
        """
        Log into Twitter account
        """

        browser = self.browser
        browser.get('https://twitter.com/')
        print('Twitter homepage loaded')
        # open twitter homepage

        username = browser.find_element_by_class_name("email-input")
        password = browser.find_element_by_name("session[password]")
        # get username and password fields

        username.clear()
        password.clear()
        # clear the fields to make sure there's not text there

        username.send_keys(self.username)
        password.send_keys(self.password)
        # fill the input boxes

        password.send_keys(Keys.ENTER)
        # hit enter


bot = LikeBot('email@email.com', 'password')
bot.login()
# create bot and log in
