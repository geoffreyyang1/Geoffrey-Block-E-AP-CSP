#Geoffrey Yang
#Word Game
#I collaborated with Michael Albornoz and Tobey Ng
import random
import sys
import json
from datetime import date

#Choices
category = {
    "NFL MVP": ["Jackson", "Mahomes", "Rodgers", "Brady", "Ryan", "Newton", "Peterson"],
    "NBA MVP": ["Embiid", "Jokic", "Antetokounmpo", "Harden", "Westbrook", "Curry", "Durant", "James"],
    "MLB MVP": ["Acuña Jr.", "Ohtani", "Goldschmidt", "Judge", "Harper", "Abreu", "Freeman", "Trout", "Bellinger"],
}
#Create the UI/menu
def menu():
    print("|| -----Word Game-----")
    print("|| -----Options-----")
    print("||  1) NFL MVP")
    print("||  2) NBA MVP")
    print("||  3) MLB MVP")
    print("||  4) random")
    print("||  5) scoreboard")
    print("||  6) Exit")
#set up the scoreboard
def scoreboard(score, name):
    today = date.today().strftime('%Y-%m-%d')
    scoreboardfile = {
            "Name" : name,
            "Score" : score,
            "Date" : today
            }

    with open("scoreboard.txt", 'a') as f:
        f.write(json.dumps(scoreboardfile))

def displayscoreboard():
    i = 0

wordcat = 0
randomwordcat = 0
otherwords = 0
#go through the choices
def frandom():
    wordcat = list(category.keys())
    randomwordcat = random.choice(wordcat)
    randomwords = list(category[randomwordcat])
    chosenword = random.choice(randomwords)
    hangman(chosenword)

def cat1():
    nflchoice = list(category["NFL MVP"])
    chosenword = random.choice(nflchoice)
    hangman(chosenword)

def cat2():
    nbachoice = list(category["NBA MVP"])
    chosenword = random.choice(nbachoice)
    hangman(chosenword)

def cat3():
    mlbchoice = list(category["MLB MVP"])
    chosenword = random.choice(mlbchoice)
    hangman(chosenword)

def winner(tries, length):
    score = tries * int(length)
    print("Your score is ", end = '')
    print(score)
    nameget = input("What is your name: ")
    scoreboard(score, nameget)

def hangman(cword):
    wordchecker = False
    wordcheckerint = 0
    mistakes = 5
    mistakedoublechecker = 0
    hangmanchoice = ["_"]
    repeatchecker = []
    repeatcheckerint = -1
    winnerchecker = 0
    f = len(cword)
    print(cword)

    for p in range (len(cword) - 1):
        hangmanchoice.append("_")

    while wordchecker == False:
        print("")
        print("--------------------------")
        for k in range (len(cword)):
            print(hangmanchoice[k], end = ' ')
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

                hangmanchoice[i] = str(lettergetter)
                mistakedoublechecker = mistakedoublechecker + 1

        if mistakedoublechecker >= 1:
            mistakes = mistakes + 0
        else:
            mistakes = mistakes - 1

        mistakedoublechecker = 0
#If they lose this is what is displayed
        if mistakes <= 0:
            print("You lost!")
            print("Your word was", end = ' ')
            print(cword)
            menu()
            interface()


        for q in range (10):
            print("")
        print("--------------------------")
        print("Mistakes Left: ", end = ' ')
        print(mistakes)

        for v in range (len(cword)):
            if ord(hangmanchoice[v]) == ord('_'):
                winnerchecker = winnerchecker + 1

#If they win this is what is displayed
        if winnerchecker == 0:
            wordchecker = True
            for e in range (10):
                print("")
            print("Congrats you won!!!")
            winner(mistakes, f)


        winnerchecker = 0

menuint = 0
programrun = True
#User interface direcotry
def interface():
    menuint = input("Please select a choice: ")
    if int(menuint) == 1:
        cat1()

    if int(menuint) == 2:
        cat2()

    if int(menuint) == 3:
        cat3()

    if int(menuint) == 4:
        frandom()

    if int(menuint) == 5:
        displayscoreboard()

    if int(menuint) == 6:
        programrun = False
        sys.exit()

while(programrun == True):
    menu()
    interface()
