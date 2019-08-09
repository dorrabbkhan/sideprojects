from requests import get
from random import randint
from pyfiglet import Figlet
        
f = Figlet(font='slant')
print(f.renderText('Ultimate Super Dad Joke Generator 5000'))

url = "https://icanhazdadjoke.com/search"

def getjoke(topic):
    """ 
    Make a GET request and retrieve JSON file.
    Then parse the JSON file and obtain and print the joke. 
    """
    response = get(url, headers={"Accept": "application/json"}, params={'term':topic})
    data = response.json()
    num = data['total_jokes']
    if num == 0:
        print(f"Aw snap! Couldn't find a joke about {topic}!")
    elif num == 1:
        jokeid = 0
        print(f'Ok, I found 1 joke about {topic}! Here it is:')
        joke = data['results'][0]['joke']
        print(joke)
    else:
        jokeid = randint(1,num) - 1
        print(f'Ok, I found {num} jokes about {topic}!')
        print(f'Here\'s one:')
        print(jokeid)
        joke = data['results'][jokeid]['joke']
        print(joke)

while True:
    while True:
        try:
            topic = input("What do you want a joke about? ")
            if topic == '':
                raise ValueError
        except ValueError:
            print("Enter something mate!")
            continue
        else:
            break
    getjoke(topic)
    while True:
        try:
            again = input("One more? (y/n) ")
            if again != 'y' and again != 'n':
                raise ValueError
        except ValueError:
            print("Enter only y or n!")
            continue
        else:
            break
    if again == 'n':
        break

print("Hope you found me funny!")
input()
