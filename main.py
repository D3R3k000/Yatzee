#By Derek Neil
from random import randint
Dice1 = 0
Dice2 = 0
Dice3 = 0
Dice4 = 0
Dice5 = 0
Dice6 = 0
DiceStatus1 = "Free"
DiceStatus2 = "Free"
DiceStatus3 = "Free"
DiceStatus4 = "Free"
DiceStatus5 = "Free"
DiceStatus6 = "Free"
GameStatus = 0
totalDice = int(Dice1) + int(Dice2) + int(Dice3) + int(Dice4) + int(Dice5) + int(Dice6)
ScoreOnes = 0
ScoreTwos = 0
ScoreThrees = 0
ScoreFours = 0
ScoreFives = 0
ScoreSixes = 0
ScoreThreeofaKind = 0
ScoreFourofaKind = 0
ScoreYatzee = 0
ScoreChance = 0
ReRollCounter = 0
def RollDice1():
    global Dice1
    global DiceStatus1
    if(DiceStatus1 == "Free"):
        rollingDice1 = randint(1,6)
        Dice1 = rollingDice1

def RollDice2():
    global Dice2
    global DiceStatus2
    if(DiceStatus2 == "Free"):
        rollingDice2 = randint(1,6)
        Dice2 = rollingDice2

def RollDice3():
    global Dice3
    global DiceStatus3
    if(DiceStatus3 == "Free"):
        rollingDice3 = randint(1,6)
        Dice3 = rollingDice3

def RollDice4():
    global Dice4
    global DiceStatus4
    if(DiceStatus4 == "Free"):
        rollingDice4 = randint(1,6)
        Dice4 = rollingDice4

def RollDice5():
    global Dice5
    global DiceStatus5
    if(DiceStatus5 == "Free"):
        rollingDice5 = randint(1,6)
        Dice5 = rollingDice5

def RollDice6():
    global Dice6
    global DiceStatus6
    if(DiceStatus6 == "Free"):
        rollingDice6 = randint(1,6)
        Dice6 = rollingDice6

def RollAllDice():
    RollDice1()
    RollDice2()
    RollDice3()
    RollDice4()
    RollDice5()
    RollDice6()
def reroll():
    global ReRollCounter
    if(ReRollCounter <=1):
        RollAllDice()
        ReRollCounter = ReRollCounter+1
    else:
        print("You can only reroll twice.")

def MainGame():
    UserCommand = input("Command:")
    global Dice1
    global Dice2
    global Dice3
    global Dice4
    global Dice5
    global Dice6
    if(UserCommand == "Start Game"):
        RollAllDice()

        print("Dice: " + str(Dice1)+" | " + str(Dice2)+" | " + str(Dice3)+" | " + str(Dice4)+" | " + str(Dice5)+" | " + str(Dice6))
    if(UserCommand == "Hold 1"):
        global DiceStatus1
        DiceStatus1 = "Held"
    if (UserCommand == "Hold 2"):
        global DiceStatus2
        DiceStatus2 = "Held"
    if (UserCommand == "Hold 3"):
        global DiceStatus3
        DiceStatus3 = "Held"
    if (UserCommand == "Hold 4"):
        global DiceStatus4
        DiceStatus4 = "Held"
    if (UserCommand == "Hold 5"):
        global DiceStatus5
        DiceStatus5 = "Held"
    if (UserCommand == "Hold 6"):
        global DiceStatus6
        DiceStatus6 = "Held"
    if(UserCommand == "Reroll"):
        reroll()

        print("Dice: " + str(Dice1) + " | " + str(Dice2) + " | " + str(Dice3) + " | " + str(Dice4) + " | " + str(
            Dice5) + " | " + str(Dice6))
    if(UserCommand == "Take 2s"):
        TwosList =[]
        TwosList.append(Dice1)
        TwosList.append(Dice2)
        TwosList.append(Dice3)

while GameStatus <= 0:
     MainGame()
