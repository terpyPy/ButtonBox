import boardFunc
from time import sleep, time
from random import randrange
class boardState():

    # include the lower level abstraction modules we made and imported    
    
    #
    # include all the named constants you know, leave as tuple cuz immutable

    # this class is a representation of the board logically, it takes the initial gamestate as an arg
    def __init__(self, theBoard):
        self.OFF = (0, 0, 0)
        self.GREEN = (0, 25, 0)
        self.WHITE = (10, 10, 10)

        self.onColor = self.WHITE
        self.offColor = self.OFF

        # gives boardState access to the theBoard and patternSize arg passed from init 
        self.theBoard = theBoard
        # number of elements in the board
        self.boardSize = len(self.theBoard)
        
        # the init method takes one argument, the game board
        self.previousTimePressed = None
        self.timePressed = None

        self.previousButtonPressed = None


    def debounce(self):#first press will always be smaller then second
        #TODO pass in time pressed from loop in main.py
        sleep(0.02)
        timebetween = time() - self.timePressed
        if timebetween >= 0.2:
            print("debounce failed, time between:",timebetween)
            return False # return toFast str if true
        else:
            print("debounce passed, time between:",timebetween)
            return True # else return true, the time between pressed is valid

    def setRandom(self):
        newBoard = self.theBoard
        # set a random value in theBoard to be onColor
        self.theBoard[randrange(0,self.boardSize-1)] = self.onColor
        return newBoard

    def checkWin(self, allLit):
        # check if the board is cleared and the previous state had all neighbors lit up
        # TODO this is redundant because the only way to clear the board is pressing a button whose neighbors are all lit up!
        if (self.onColor not in self.theBoard) and allLit:
           return True

    def clearArray(self):
        self.theBoard = [self.offColor] * self.boardSize
        
    def doGameLogic(self, event):
        self.timePressed = time()
        # takes theboard and "event" or pressed button as an argument,
        # and returns the updated board state
        print("")
        print("doGameLogic start time",self.timePressed)
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


