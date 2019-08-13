"""
Scrapes book price and name from books.toscrape.com
using Scrapy and stores them in a csv file. Use 
scrapy runspider -o books.csv bookscrape.py to execute.
"""

import scrapy, time
# import dependencies

class BookSpider(scrapy.Spider):
    # create scraper class

    name = 'bookspider'
    start_urls = ["http://books.toscrape.com"]
    # set the starting url

    def parse(self, response):
        # function for parsing the data on the page

        for article in response.css('article.product_pod'):
            # iterate through the articles on the page

            yield {
                'price': article.css(".price_color::text").extract_first(),
                'title': article.css("h3 > a::attr(title)").extract_first()
                # obtain price and title of the current book article
            }
        next = response.css('.next > a::attr(href)').extract_first()
        # set next page's url

        if next:
            time.sleep(0.5)
            yield response.follow(next, self.parse)
            # delay by 0.5s and scrape the next page if the link for the 
            # next page is found 