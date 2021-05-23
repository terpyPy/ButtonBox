import boardFunc
from time import time
from random import randrange
class boardState():

    # include the lower level abstraction modules we made and imported    
    
    #
    # include all the named constants you know, leave as tuple cuz immutable

    # this class is a representation of the board logically, it takes the initial gamestate as an arg
    def __init__(self, theBoard):
        self.OFF = (0, 0, 0)
        self.GREEN = (0, 25, 0)
        self.WHITE = (127, 127, 127)

        self.onColor = self.WHITE
        self.offColor = self.OFF

        # gives boardState access to the theBoard and patternSize arg passed from init 
        self.theBoard = theBoard
        
        # the init method takes one argument, the game board
        self.previousTimePressed = None
        self.timePressed = None

        self.previousButtonPressed = None


    def debounce(self):#first press will always be smaller then second
        timebetween = int(time()) - int(self.timePressed)
        if timebetween >= 0.4:
            return 'tooFast' # return toFast str if true
        else:
            return True # else return true, the time between pressed is valid

    def setRandom(self):
        newBoard = self.theBoard
        self.theBoard[randrange(0,15)] = self.onColor
        return newBoard

    def checkWin(self, allLit):
        if self.onColor not in self.theBoard:
           return True

    def clearArray(self):
        self.theBoard = boardFunc.resetBoard()
        
    def doGameLogic(self, event):
        self.timePressed = time()
        # takes theboard and "event" or pressed button as an argument,
        # and returns the updated board state
        if self.debounce():
            print("event number:",event.number)
            print("prev pressed:",self.previousButtonPressed)
            if not event.number == self.previousButtonPressed:
                self.previousButtonPressed = event.number
                self.theBoard, allNeighborsLit = boardFunc.gameLogic(self.theBoard, event, self.onColor, self.offColor)
                if self.checkWin(allNeighborsLit):
                    print("win condition met logically")
                    for i in range(16):
                        self.theBoard[i] = self.GREEN
                    #print(self.theBoard)


