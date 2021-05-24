import boardFunc
from time import time
import digitalio
import board
from random import randrange
class boardState():

    # include the lower level abstraction modules we made and imported    
    # define static tuples for colors

    # this class is a logical representation of the board, it takes the initial gamestate as an arg
    def __init__(self, theBoard):

        self.onColor = (50,50,50)
        self.offColor = (0,0,0)
        self.winColor = (0, 25, 0)
        
        # create nuke button attributes:
        #   tell the board which physical pin address to read for button input
        self.button_pin = board.D6
        #   instantiate an object version of the button as a digitalIO object reading from given pin
        self.button = digitalio.DigitalInOut(self.button_pin)
        #   define the button as an input button
        self.button.direction = digitalio.Direction.INPUT
        #   define the button 
        self.button.pull = digitalio.Pull.UP

        # gives boardState access to the theBoard and patternSize arg passed from init 
        self.theBoard = theBoard
        
        # the init method takes one argument, the game board
        self.patternSize = 1
        self.timePressed = time()

        self.previousButtonPressed = None

    def debounce(self):
        # filters button inputs, input will only be accepted every 0.2 seconds as measured from last press
        if time() - self.timePressed > 0.2:
            return True
        else:
            return False 

    def checkWin(self):
        # check logical board against win condition, in this case if the board is empty
        if self.onColor not in self.theBoard:
           return True

    # random pattern game init
    def randomStart(self):
        self.theBoard[randrange(0,15)] = self.onColor

    def clearBoard(self):
        # return a list representation of a blank board
        self.theBoard = [(0,0,0)]*16

    def doGameLogic(self, event):
        # takes theboard and "event" or pressed button as an argument and updates the board state
         if self.debounce():
             # check if the player is pressing the same button they did last turn
            if not event.number == self.previousButtonPressed:
                # if not then do the main game logic
                self.previousButtonPressed = event.number
                self.theBoard = boardFunc.gameLogic(self.theBoard, event, self.onColor, self.offColor)
                if self.checkWin():
                    # if a win is registered set the whole board to the win color
                    for i in range(16):
                        self.theBoard[i] = self.winColor
            # update the last pressed time for debouncing purposes 
            self.timePressed = time()


