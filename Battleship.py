#Mitchell Foley
#1316506
#foleymb
#
#BattleShip
#

class player():
   def __init__(self):
       self.myFleet = [[None]*7]*7
       self.myHits = [[None]*7]*7

#def main():
#    printIntro()
#    setup()
#    game()
#    printResults()

def printIntro():
    print("This is a game of BattleShip, you versus the computer. ")
    print("You will select the placements of a Destroyer of size 2,")
    print(" a Cruiser of size 3, and an Aircraft Carrier of size 5.")
    print("The game board is 7x7 each.")
    print("The computer will start first after ships have been placed.")

def setup():
    players = createPlayers()
    for i in range(2):
        players[i] = placeShips(players[i])

def createPlayers():
    A = player()
    B = player()
    return [A,B]

def placeShips(p):
    selection = getShipInfo()
    #add ships to p.myFleet
    return p

def getShipInfo():
    d,dr = input("Where do you want to place your size 2 (D)estroyer? (ie. (1,1)) : "),input("(H)orizontally or (V)ertically?: ")
    a,ar = input("Where do you want to place your size 5 (A)ircraft Carrier (ie. (1,1)) : "),input("(H)orizontally or (V)ertically?: ")
    c,cr = input("Where do you want to place your size 3 (C)ruiser? (ie. (1,1)) : "),input("(H)orizontally or (V)ertically?: ")
    return ((d,dr),(a,ar),(c,cr))

    
