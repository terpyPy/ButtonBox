import boardFunc
import time
class boardState():

    # include the lower level abstraction modules we made and imported    
    
    #
    # include all the named constants you know, leave as tuple cuz immutable

    # this class is a representation of the board logically, it takes the initial gamestate as an arg
    def __init__(self, theBoard):
        self.OFF = (0, 0, 0)
        self.RED = (25, 0, 0)
        self.YELLOW = (25, 15, 0)
        self.GREEN = (0, 25, 0)
        self.CYAN = (0, 25, 25)
        self.BLUE = (0, 0, 25)
        self.PURPLE = (18, 0, 25)
        self.WHITE = (127, 127, 127)

        self.onColor = self.WHITE
        self.offColor = self.OFF

        # gives boardState access to the theBoard and patternSize arg passed from init 
        self.theBoard = theBoard
        
        # the init method takes one argument, the game board
        self.patternSize = 1
        self.previousTimePressed = None
        self.timePressed = None


    def timeBetweenPress(self):#first press will always be smaller then second
        timebetween = int(time.time()) - self.timePressed
        if timebetween >= 0.2:
            return 'tooFast' # return toFast str if true
        else:
            return True # else return true, the time between pressed is valid

    # random pattern game init
    def randomArray(self):
        # return the value of getRandomPatt
        return boardFunc.randGamePattern(self.patternSize)

    def clearArray(self, offColor, onColor):
        self.theBoard = boardFunc.resetBoard(self.theBoard, offColor, onColor)
        
    def gameLogic(self, event):
        self.timePressed = time.time()
        # takes theboard and "event" or pressed button as an argument,
        # and returns the updated board state
        if self.timeBetweenPress():
            return boardFunc.gameLogic(self.theBoard, event, self.onColor, self.offColor)

