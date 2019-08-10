import requests
from bs4 import BeautifulSoup
import csv

"""
Scraper to scrape quotes from url below and to
save the scraped data into a file called data.csv.
Uses BeautifulSoup to scrape.
"""

def scrape():
    # function to scrape data from the belowmentioned url
    # using beautifulsoup and requests

    site = "http://quotes.toscrape.com"
    response = requests.get(site)
    soup = BeautifulSoup(response.text, "html.parser")
    quotes = soup.select(".quote")
    # setup initial variables and request and parse the first page
    # also select all elements with quote class on the page

    with open("data.csv", "w+", newline='') as f:
        # open file to write data into

        csv_writer = csv.writer(f)
        csv_writer.writerow(["quote", "author_f", "author_l", "author_link"])
        reached_end = False
        # write column headings, and set the end of scraping flag to false

        while not reached_end:
            for quote in quotes:
                # increment for each scraped quote element

                quote_text = quote.find("span")
                quote_text = quote_text.get_text()
                # extract the quote's text

                author = quote.select(".author")[0].get_text()
                author = author.split(" ")
                # extract the author name and split into different words

                if len(author) > 2:
                    author = ' '.join(author[0:-1]), author[-1]
                    # if author has more than 2 words in name, join the first
                    # n-1 words into first name and the last word into last name

                author_f, author_l = author
                # extract author names

                url = quote.find("a").attrs["href"]
                url = site + url
                # extract url for the author's biography page

                try:
                    csv_writer.writerow([quote_text, author_f, author_l, url])
                    # write the quote, author's first name, last name and
                    # the url of their biography page into the csv file
                    
                except UnicodeEncodeError:
                    pass
                # skip over records that have strings that can't be encoded
                # by Python

            try:
                next_url = site + soup.select(".next")[0].find("a")["href"]
                # set up the url of the next page for further scraping

            except IndexError:
                reached_end = True
                break
            # scrape further until end is reached and IndexError is given
            # on BeautifulSoup's select function's reterned value
            # if end is reached, then break out of the while loop

            response = requests.get(next_url)
            # request next page

            print(next_url)
            # print next page's url

            soup = BeautifulSoup(response.text, "html.parser")
            # parse the loaded page

            quotes = soup.select(".quote")
            # update the quotes variable with the new page's quotes
