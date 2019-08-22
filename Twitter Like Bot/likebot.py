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

        self.profile = webdriver.FirefoxProfile()
        self.profile.set_preference("browser.privatebrowsing.autostart", True)
        self.browser = webdriver.Firefox(firefox_profile=self.profile)


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
        time.sleep(10)
        # hit enter and wait for page to load


    def like_tweet(self, hashtag):
        """
        Method for liking all tweets given a hashtag
        """

        browser = self.browser
        browser.get(f'https://twitter.com/search?q={hashtag}&src=typed_query')
        # open the URL for the hashtag

        for i in range(3):
            browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
            time.sleep(5)
        # scroll down and wait 5 s three times

        like_buttons = browser.find_elements_by_xpath("//div[@data-testid='like']")
        # find all like buttons by custom attribute "data-testid='like'"

        for like_button in like_buttons:
            like_button.click()
            # click all like buttons


def execute_bot():
    """
    Execute the script and like all tweets
    """
    bot = LikeBot('email@email.com', 'password')
    bot.login()
    bot.like_tweet('hashtag')
    # create bot, log in and like tweets


if __name__ == "__main__":
    execute_bot()
    