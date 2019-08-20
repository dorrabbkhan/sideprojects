"""
Simple blackjack game, runs until player runs out of credits
Start with 100 credits
"""

import random

SUIT = ['Spades', 'Hearts', 'Diamonds', 'Clubs']


class Card():

    '''
    Class for a card
    '''

    def __init__(self):

        self.suit = ''
        self.num = 0
        # initialize suit and number as empty

    def set(self, suit, num):
        '''
        Set suit and number for card
        '''

        self.suit = suit
        self.num = num

    def __str__(self):

        return f"{self.num} of {self.suit}"
        # return string representation of the card


class Deck():

    '''
    Class for a deck
    '''

    def __init__(self):

        self.cards = []
        # initialize list of cards in this deck

        for i in range(4):
            # for each suit

            for j in range(10):
                # for each card

                new_card = Card()
                new_card.set(SUIT[i], j+1)
                self.cards.append(new_card)
                # create a new card and append it to this deck

        for k in range(3):
            # for 3 cards

            for l in range(4):
                # for each suit

                new_card = Card()
                new_card.set(SUIT[l], 10)
                self.cards.append(new_card)
                # create a card with value 10 and append it to this deck

    def reset(self):
        '''
        Reset deck to original
        '''

        self.__init__()

    def __str__(self):

        out = ''
        for i in self.cards:
            # for each card

            out = out + (f"{i.num} of {i.SUIT}\n")
            # create output line

        return out
        # return output

    def shuffle(self):
        '''
        Shuffle deck
        '''

        random.shuffle(self.cards)

    def pop(self):
        '''
        Pop card from deck
        '''

        return self.cards.pop()


class Player():

    '''
    Class for a player
    '''

    def __init__(self):

        self.hand = []
        self.credit = 100
        self.bet = 0
        # initialize player's hand, credit and bet

    def reset(self):
        '''
        Reset player's hand
        '''

        self.hand = []

    def deal(self, num):
        '''
        Deal num number of cards
        '''

        for i in range(num):
            # for each card to be dealt

            card = MYDECK.pop()
            self.hand.append(card)
            # pop from the deck and append to player's hand

    def showcards(self, num):
        '''
        Show the first num number of cards in hand
        '''

        j = 0
        # initialize count

        for i in self.hand:
            j += 1
            print(i)
            # increment count and print card

            if j == num:
                break
                # end if num number of cards have been shown

    def withdraw(self, bet):
        '''
        Remove bet credits from player's credits
        '''
        self.bet = bet
        self.credit -= bet
        print(f"\nNew balance is {self.credit}")
        # set bet, remove from credit and print new balance

    def showall(self):
        '''
        Print all cards in player's hand
        '''
        for i in self.hand:
            print(i)
            # print all cards

    def checkbust(self):
        '''
        Check if player is busted
        '''
        total = 0
        # initialize sum of card numbers

        for i in self.hand:
            total += i.num
            # for each card, add it's number to total

        print(f"\nNew sum is {total}")
        # print new sum of cards

        return total <= 21
        # return whether total is <= 21 or not to determine bust

    def givesum(self):
        '''
        Return sum of player's hand
        '''

        total = 0
        # initialize total

        for i in self.hand:
            total += i.num
            # for each card in hand, add its number to total

        return total

    def double(self):
        '''
        Increment player's credits by 2*bet
        '''
        self.credit += self.bet*2


HUMAN = Player()
COMPUTER = Player()
MYDECK = Deck()
# initialize human, computer and deck


def askbet():
    '''
    Ask player for bet
    '''

    while True:

        try:
            bet = int(input('\nHow much would you like to bet? '))
            # input bet

        except ValueError:
            print("\nPlease enter an integer!")
            continue
            # assert integer input

        else:
            if bet > HUMAN.credit:
                print("\nToo much bet!")
                continue
                # assert bet to be less than current credit

            else:
                HUMAN.withdraw(bet)
                break
                # withdraw bet from credits and break out of loop

    return bet


def dealtwo():
    '''
    Deal two cards each and show one x computer and two x player
    '''

    HUMAN.deal(2)
    print("\nHuman cards:")
    HUMAN.showcards(2)
    # deal two cards to human, and print both cards

    COMPUTER.deal(2)
    print("\nComp cards:")
    COMPUTER.showcards(1)
    # deal two cards to computer, and print one card


def askforhit():
    '''
    Ask player for hit or stay
    '''

    safe = True
    # set safe (not busted) to true

    while True and safe:

        choice = input("\nWould you like to hit or stay? (H/S)")
        # input H or S for hit or stay

        if choice == 'H':

            HUMAN.deal(1)
            HUMAN.showall()
            safe = HUMAN.checkbust()
            continue
            # deal one card, show all cards, and check if human is busted

        elif choice == 'S':

            playdealer()
            break
            # play dealer's turn

        else:

            print("\nBad choice!")
            continue
            # take input again if input is not 'H' or 'S'

    if not safe:
        print("\nBUSTED, GAME OVER!")
        # if player is busted then print game over


def playdealer():
    '''
    Play computer's turn
    '''

    while COMPUTER.givesum() < 17:
        # keep dealing until sum gets greater than 17

        COMPUTER.deal(1)
        COMPUTER.showall()
        # deal one card and show all computer cards

        print(f"\nComputer's sum is {COMPUTER.givesum()}")
        # print computer's sum of cards in hand

    if not COMPUTER.checkbust():
        # if computer is busted

        print("\nComputer BUSTED! You won!")
        HUMAN.double()
        # print win message and increase human's credits

    else:
        checkwin()
        # check who won


def checkwin():
    '''
    Check who won
    '''

    if COMPUTER.givesum() < HUMAN.givesum():
        print("\nHuman won!")
        HUMAN.double()
        # if human's sum is greater, print win message and increase credit

    elif COMPUTER.givesum() > HUMAN.givesum():
        print("\nComputer won!")
        # if computer's sum is greater, print win message

    else:
        print("\nDraw!")
        # print draw message if sums are equal


def engine():
    '''
    Main game engine
    '''

    credit = True
    # set flag for if credit remains to be true

    while True and credit:

        print(f'\nNew balance is {HUMAN.credit}')
        # print new balance

        MYDECK.reset()
        HUMAN.reset()
        COMPUTER.reset()
        # reset deck and hands

        MYDECK.shuffle()
        bet = askbet()
        # shuffle deck and ask for bet

        print(f"\nYou bet {bet} chips!")
        # show how many chips were bet

        dealtwo()
        askforhit()
        # deal two cards each and ask for hit

        credit = HUMAN.credit > 0
        # set the boolean for if credit remains or not

    print("\nGAME OVER")
    # print game over if ran out of credit


engine()
# call main engine of game
