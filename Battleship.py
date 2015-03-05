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


#def setup():
#    player = [None,None]
#    
#    for i in range(2):
#         player[i] = createPlayer(i)
#def createPlayer(pl):
#    myFleet = [[None*7]*7]
#    myHits = [[None*7]*7]
#    myFleet[0],myFleet[1] = placeShips()
#        
