""" Simple blackjack game, runs until player runs out of credits
Start with 100 credits """
import random
SUIT = ['Spades', 'Hearts', 'Diamonds', 'Clubs']

class Card():

    '''
    Class for a card
    '''

    def __init__(self):
        self.suit = ''
        self.num = 0
    def set(self, suit, num):
        '''
        Set suit and number for card
        '''
        self.suit = suit
        self.num = num
    def __str__(self):
        return f"{self.suit} and {self.num}"

class Deck():

    '''
    Class for a deck
    '''

    def __init__(self):
        self.cards = []
        for i in range(4):
            for j in range(10):
                new_card = Card()
                new_card.set(SUIT[i], j+1)
                self.cards.append(new_card)
        for k in range(3):
            for l in range(4):
                new_card = Card()
                new_card.set(SUIT[l], 10)
                self.cards.append(new_card)

    def reset(self):
        '''
        Reset deck to original
        '''
        self.__init__()

    def __str__(self):
        out = ''
        for i in self.cards:
            out = out + (f"{i.SUIT} and {i.num}\n")
        return out

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
            card = MYDECK.pop()
            self.hand.append(card)

    def showcards(self, num):
        '''
        Show the first num number of cards in hand
        '''
        j = 0
        for i in self.hand:
            j += 1
            print(i)
            if j == num:
                break

    def withdraw(self, bet):
        '''
        Remove bet credits from player's credits
        '''
        self.bet = bet
        self.credit -= bet
        print(f"\nNew balance is {self.credit}")

    def showall(self):
        '''
        Print all cards in player's hand
        '''
        for i in self.hand:
            print(i)

    def checkbust(self):
        '''
        Check if player is busted
        '''
        total = 0
        for i in self.hand:
            total += i.num
        print(f"\nNew sum is {total}")
        return total <= 21

    def givesum(self):
        '''
        Return sum of player's hand
        '''
        total = 0
        for i in self.hand:
            total += i.num
        return total

    def double(self):
        '''
        Increment player's credits by 2*bet
        '''
        self.credit += self.bet*2

HUMAN = Player()
COMPUTER = Player()
MYDECK = Deck()

def askbet():
    '''
    Ask player for bet
    '''
    while True:
        try:
            bet = int(input('\nHow much would you like to bet? '))
        except ValueError:
            print("\nPlease enter an integer!")
            continue
        else:
            if bet > HUMAN.credit:
                print("\nToo much bet!")
                continue
            else:
                HUMAN.withdraw(bet)
                break
    return bet

def dealtwo():
    '''
    Deal two cards each and show one x computer and two x player
    '''
    HUMAN.deal(2)
    print("\nHuman cards:")
    HUMAN.showcards(2)
    COMPUTER.deal(2)
    print("\nComp cards:")
    COMPUTER.showcards(1)

def askforhit():
    '''
    Ask player for hit or stay
    '''
    safe = True
    while True and safe:
        choice = input("\nWould you like to hit or stay? (H/S)")
        if choice == 'H':
            HUMAN.deal(1)
            HUMAN.showall()
            safe = HUMAN.checkbust()
            continue
        elif choice == 'S':
            playdealer()
            break
        else:
            print("\nBad choice!")
            continue
    if not safe:
        print("\nBUSTED, GAME OVER!")

def playdealer():
    '''
    Play computer's turn
    '''
    while COMPUTER.givesum() < 17:
        COMPUTER.deal(1)
        COMPUTER.showall()
        print(f"\nComputer's sum is {COMPUTER.givesum()}")
    if not COMPUTER.checkbust():
        print("\nComputer BUSTED! You won!")
        HUMAN.double()
    else:
        checkwin()

def checkwin():
    '''
    Check who won
    '''
    if COMPUTER.givesum() < HUMAN.givesum():
        print("\nHuman won!")
        HUMAN.double()
    elif COMPUTER.givesum() > HUMAN.givesum():
        print("\nComputer won!")
    else:
        print("\nDraw!")


def engine():
    '''
    Main game engine
    '''
    credit = True
    while True and credit:
        print(f'\nNew balance is {HUMAN.credit}')
        MYDECK.reset()
        HUMAN.reset()
        COMPUTER.reset()
        MYDECK.shuffle()
        bet = askbet()
        print(f"\nYou bet {bet} chips!")
        dealtwo()
        askforhit()
        credit = HUMAN.credit > 0
    print("\nGAME OVER")

engine()
