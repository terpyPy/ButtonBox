import simMyBoard
import boardChecks
import gameFunction
class boardState():
    # include the lower level abstraction modules we made and imported
    boardChecks
    gameFunction

    
    # include all the named constants you know, leave as tuple cuz immutable
    OFF = (0, 0, 0)
    RED = (25, 0, 0)
    YELLOW = (25, 15, 0)
    GREEN = (0, 25, 0)
    CYAN = (0, 25, 25)
    BLUE = (0, 0, 25)
    PURPLE = (18, 0, 25)
    WHITE = (127, 127, 127)
    def __init__(self, theBoard):
    
        # gives boardState access to the theBoard arg passed from init 
        self.theBoard = theBoard
        
        
        
        # the init method takes one argument, the game board
        self.COLORS = [self.RED, self.YELLOW, self.GREEN, self.CYAN, self.BLUE, self.PURPLE]
        self.animColor = self.WHITE
        self.rightColor = self.GREEN
        self.wrongColor = self.RED
    # random pattern game init
    def randomArray(self):
        # return the value of getRandomPatt
        return gameFunction.getRandomPatt()
    def clearArray(self):
        return boardChecks.reset(x.theBoard)
    

        

x = boardState([0] * 16)
pattern = x.randomArray()
print(pattern)
for i in range(len(x.theBoard)):
    x.theBoard = simMyBoard.checkBoard(pattern, i, x.theBoard)
print(x.theBoard, "before reset")
x.theBoard = x.clearArray()
print(x.theBoard)