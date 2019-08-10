import random
import requests
import csv
import bs4
import scrape

"""
Main driver function for the quote's author guessing
game. Uses scrape.py to generate data and reads it
to build a game where the user has 4 tries to guess
the author of a random quote. The user is given a hint
after each wrong guess.
"""


def gen_hint(guesses, quote):
    # function to generate a hint

    first_name = quote[1]
    last_name = quote[2]
    url = quote[3]
    # separate quote variable into first name,
    # last name and the biography page's url

    if guesses == 3:
        response = requests.get(url)
        # request the author's biography page

        soup = bs4.BeautifulSoup(response.text, "html.parser")
        # parse the biography page

        birth_location = soup.select(".author-born-location")[0].get_text()
        # extract the birth location of the author

        birth_date = soup.select(".author-born-date")[0].get_text()
        # extract the birth date of the author

        return(f"The author was born {birth_location} on {birth_date}")
        # return a first hint of the author's birth location and date

    if guesses == 2:
        return(f"The first letter of the author's first name is {first_name[0]}")
        # return the first letter of the author's first name as the second hint

    if guesses == 1:
        return(f"The first letter of the author's last name is {last_name[0]}")
        # return the first letter of the author's last name as the last hint


scrape.scrape()
# scrape data and store into csv file

with open("data.csv") as f:
    # open the csv file for reading

    csv_reader = csv.reader(f)
    quotes = []
    # initialize csv reader, and the array to store all quotes

    for quote in csv_reader:
        quotes.append(quote)
        # fill the quotes array with records from the csv file

    while True:
        quote = random.choice(quotes)
        quote_text = quote[0]
        first_name = quote[1]
        last_name = quote[2]
        print("Ok, so the quote is:\n" + quote_text)
        # choose and print a random quote's text

        author = first_name + ' ' + last_name
        # collect author's first and last name into a single variable

        guesses = 4
        won = False
        # initialize guesses and the won flag

        while guesses > 0:
            # repeat until guesses are exhausted

            guess = input(f"Who said this? Guesses remaining: {guesses}.\n")
            # input a guess

            guesses -= 1
            # decrement guesses

            if guess.title() == author:
                # check equality of author's name with titled version of
                # the user's guess

                print("Congratulations! Correct guess!")
                won = True
                break
                # if the guess is correct, print congratulations message,
                # set win flag to true and break out of the loop

            print("Wrong guess!")
            print("Here's a hint:")
            print(gen_hint(guesses, quote))
            # generate a hint if the guess is wrong by calling the
            # gen_hint function with the number of guesses and the quote's
            # data

        if not won:
            print(f"Aw snap! You lost! The author was {author}.")
            # print if guesses are exhausted and user didn't win

        while True:
            again = input("Play again? (y/n)")
            # ask user to play again

            if again == 'y':
                break
                # repeat outer while loop if user wants to play again

            elif again == 'n':
                print("Thank you for playing!")
                input()
                exit()
                # print message, wait for input and exit if user is
                # done playing

            else:
                print("Please enter a correct input!")
                # print message and repeat the input loop if input is not
                # correct
