"""
Python script to automatically like tweets that contain
a specific hashtag. Made with selenium and geckodriver
"""

from sys import argv
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class LikeBot:
    """
    Class for twitter hashtag liking bot
    """

    def __init__(self):

        print('Initializing bot and launching Firefox')
        self.profile = webdriver.FirefoxProfile()
        self.profile.set_preference("browser.privatebrowsing.autostart", True)
        self.browser = webdriver.Firefox(firefox_profile=self.profile)
        # set profile to private and start firefox

        self.login_wait = 10
        self.scroll_wait = 5
        # set delays for logging in and scrolling

    def _get_twitter_homepage(self):
        """
        Go to twitter.com
        """

        print('Loading Twitter homepage')
        browser = self.browser
        browser.get('http://twitter.com/')

    def login(self, username, password):
        """
        Log into Twitter account
        """

        self._get_twitter_homepage()
        # open homepage

        browser = self.browser
        username_field = browser.find_element_by_class_name("email-input")
        password_field = browser.find_element_by_name("session[password]")
        # get username and password fields

        username_field.clear()
        password_field.clear()
        # clear the fields to make sure there's not text there

        username_field.send_keys(username)
        password_field.send_keys(password)
        # fill the input boxes

        password_field.send_keys(Keys.ENTER)
        time.sleep(self.login_wait)
        # hit enter and wait for page to load

    def like_tweet(self, hashtag, scroll_limit):
        """
        Method for liking all tweets given a hashtag
        """

        print(f'Opening search page for #{hashtag}')
        browser = self.browser
        browser.get(f'https://twitter.com/search?q={hashtag}&src=typed_query')
        # open the URL for the hashtag

        print('Scrolling down')
        for i in range(scroll_limit):
            browser.execute_script(
                'window.scrollTo(0, document.body.scrollHeight)')
            time.sleep(scroll_wait)
        # scroll down and wait scroll_wait seconds three times

        print('Finding like buttons')
        like_buttons = browser.find_elements_by_xpath(
            "//div[@data-testid='like']")
        # find all like buttons by custom attribute "data-testid='like'"

        print('Liking tweets')
        for like_button in like_buttons:
            like_button.click()
            # click all like buttons

    def logout(self):
        """
        Log out of current Twitter session
        """

        print('Logging out of Twitter')
        browser = self.browser
        browser.get('http://www.twitter.com/logout')
        # go to logout page

        logout_button = browser.find_elements_by_xpath(
            "//div[@data-testid='confirmationSheetConfirm']")
        logout_button.click()
        # click logout button


def execute_bot(username, password, hashtag, scroll_limit):
    """
    Execute the script and like all tweets
    """

    bot = LikeBot()
    bot.login(username, password)
    bot.like_tweet(hashtag, scroll_limit)
    bot.logout()
    # create bot, log in, like tweets and logout


if __name__ == "__main__":

    username, password, hashtag, scroll_limit = tuple(argv[1:5])
    execute_bot(username, password, hashtag, scroll_limit)
    # get arguments from command line and execute bot
