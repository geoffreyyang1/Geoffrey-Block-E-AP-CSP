#Geoffrey Yang
#I collaborated with Michael ALbornoz and Tobey Ng
import random
import sys
import os.path
import json
from datetime import date

category = {
    "NFL MVP": ["Jackson", "Mahomes", "Rodgers", "Brady", "Ryan", "Newton", "Peterson"],
    "NBA MVP": ["Embiid", "Jokic", "Antetokounmpo", "Harden", "Westbrook", "Curry", "Durant", "James"],
    "MLB MVP": ["Acuña Jr.", "Ohtani", "Goldschmidt", "Judge", "Harper", "Abreu", "Freeman", "Trout", "Bellinger"],
}

def menu():
    print("Word Game")
    print("Options")
    print("1: NBA MVP")
    print("2: NFL MVP")
    print("3: MLB MVP")
    print("4: Random")
    print("5: Scoreboard")
    print("6: Exit")

def scoreboard(score, name):
    today = date.today().strftime('%Y-%m-%d')
    scoreboardorg = {
            "Name" : name,
            "Score" : score,
            "Date" : today
            }
    for t in range (100):
        if os.path.isfile(t.txt) == False:
            with open(t.txt, 'a') as f:
                f.write(json.dumps(scoreboardorg))
                f.write("\n")

def scoreboarddisplay():
    with open('scoreboard.txt', 'r') as f:
        for line in f.readlines():
            data = f.read()
            js = json.loads(data)
            print(js)


wordpick = 0
randomwordpick = 0
otherwords = 0
def random():
    wordpick = list(category.keys())
    randomwordpick = random.choice(wordpick)
    randomwords = list(category[randomwordpick])
    wordchoice = random.choice(randomwords)
    hangman(wordchoice)

def cat1():
    nfl = list(category["NFL"])
    wordchoice = random.choice(nfl)
    hangman(wordchoice)

def cat2():
    nba = list(category["NBA"])
    wordchoice = random.choice(nba)
    hangman(wordchoice)

def cat3():
    mlb = list(category["MLB"])
    wordchoice = random.choice(mlb)
    hangman(wordchoice)

def win(tries, length):
    score = tries * int(length)
    print("Your score is ", end = '')
    print(score)
    name = input("What is your name: ")
    scoreboard(score, name)

def hangman(cword):
    wordchecker = False
    wordcheckerint = 0
    mistakes = 5
    mistakedoublechecker = 0
    hangmanword = ["_"]
    repeatchecker = []
    repeatcheckerint = -1
    winnerchecker = 0
    f = len(cword)
    print(cword)

    for p in range (len(cword) - 1):
        hangmanword.append("_")

    while wordchecker == False:
        print("")
        print("--------------------------")
        for k in range (len(cword)):
            print(hangmanword[k], end = ' ')
        lettergetter = input("Please type a letter: ")
        print("--------------------------")

        repeatcheckerint = repeatcheckerint + 1
        repeatchecker.append(lettergetter)
        print(repeatchecker)

        for j in range (repeatcheckerint):
            if ord(lettergetter) == ord(repeatchecker[j]):
                print("No repeats")
                mistakes = mistakes - 1
                break

        for i in range (len(cword)):
            if ord(cword[i]) == ord(lettergetter):

                hangmanword[i] = str(lettergetter)
                mistakedoublechecker = mistakedoublechecker + 1

        if mistakedoublechecker >= 1:
            mistakes = mistakes + 0
        else:
            mistakes = mistakes - 1

        mistakedoublechecker = 0

        if mistakes <= 0:
            print("Oh No!!! You lost :(")
            print("Your word was -------> ", end = ' ')
            print(cword)
            menu()
            interface()


        for q in range (10):
            print("")
        print("-----")
        print("Mistakes Left: ", end = ' ')
        print(mistakes)

        for v in range (len(cword)):
            if ord(hangmanword[v]) == ord('_'):
                winnerchecker = winnerchecker + 1


        if winnerchecker == 0:
            wordchecker = True
            for e in range (10):
                print("")
            print("You won")
            win(mistakes, f)


        winnerchecker = 0

menuint = 0
programrun = True

def instructions():
    print("Instructions")

def interface():
    menuint = input("Please select a choice: ")
    if int(menuint) == 1:
        cat1()

    if int(menuint) == 2:
        cat2()

    if int(menuint) == 3:
        cat3()

    if int(menuint) == 4:
        random()

    if int(menuint) == 5:
        scoreboarddisplay()

    if int(menuint) == 6:
        instructions()

    if int(menuint) == 7:
        programrun = False
        sys.exit()

while(programrun == True):
    menu()
    interface()
