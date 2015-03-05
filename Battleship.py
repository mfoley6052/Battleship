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
    lengths = [2,5,3]
    valid = []
    selection = getShipInfo()
    for i in range(len(selection)):
        p = checkPlacement(p,selection[i],lengths[i])
        
    return p

def checkPlacement(p,data,l):
    if data[1] == "H" or data[1] == "h":
        if data[0][0] + l <= 6:
            for i in range(l):
                p.myFleet[data[0][0]+i][data[0][1]]
        elif data[0][0] - l >= 0:
            for i in range(l-1,-1,-1):
                p.myFleet[data[0][0]+i][data[0][1]]
        else:
            return False
    elif data[1] == "V" or data[1] == "v":
        if data[0][1] + l <=6:
            for i in range(l):
                p.myFleet[data[0][0]][data[0][1]+i]
        elif data[0][1] - l >= 0:
            for i in range(l-1,-1,-1):
                p.myFleet[data[0][0]][data[0][1]+i]
        else:
            return False
    return p

def getShipInfo():
    d,dr = input("Where do you want to place your size 2 (D)estroyer? (ie. (1,1)) : "),input("(H)orizontally or (V)ertically?: ")
    a,ar = input("Where do you want to place your size 5 (A)ircraft Carrier (ie. (1,1)) : "),input("(H)orizontally or (V)ertically?: ")
    c,cr = input("Where do you want to place your size 3 (C)ruiser? (ie. (1,1)) : "),input("(H)orizontally or (V)ertically?: ")
    return ((d,dr),(a,ar),(c,cr))

    
