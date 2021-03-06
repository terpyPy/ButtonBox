import boardFunc
class boardState():

    # include the lower level abstraction modules we made and imported    
    boardFunc
    #
    # include all the named constants you know, leave as tuple cuz immutable
    OFF = (0, 0, 0)
    RED = (25, 0, 0)
    YELLOW = (25, 15, 0)
    GREEN = (0, 25, 0)
    CYAN = (0, 25, 25)
    BLUE = (0, 0, 25)
    PURPLE = (18, 0, 25)
    WHITE = (127, 127, 127)

    # this class is a representation of the board logically, it takes the initial gamestate as an arg
    def __init__(self, theBoard):
        
        # gives boardState access to the theBoard and patternSize arg passed from init 
        self.theBoard = theBoard
        
        # the init method takes one argument, the game board
        self.COLORS = [self.RED, self.YELLOW, self.GREEN, self.CYAN, self.BLUE, self.PURPLE]
        self.animColor = self.WHITE
        self.rightColor = self.GREEN
        self.wrongColor = self.RED

    # random pattern game init
    def randomArray(self):
        # return the value of getRandomPatt
        return boardFunc.randGamePattern(self.patternSize)

    def clearArray(self):

        # takes the board as and arg and returns it with all positions off
        return boardFunc.resetBoard(self.theBoard)
    def redrawBoard(self, event):
        
        # takes theboard and "event" or pressed button as an argument,
        # and returns the updated board state
        return boardFunc.redrawBoard(self.theBoard, event)

