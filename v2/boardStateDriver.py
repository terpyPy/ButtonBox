# from random import randrange
from boardFunc.gameOptions import games
from time import time, sleep
from random import randrange
class boardState():
    # this class is a representation of the board logically, it takes the initial gamestate as an arg
    # the init method takes one argument, the game board
    def __init__(self, theBoard):
        self.OFF = (0, 0, 0)
        self.GREEN = (0, 25, 0)
        self.WHITE = (12, 12, 12)
        self.onColor = self.WHITE
        self.offColor = self.OFF
        #
        # we have an object that takes args from here as they are logically constructed and the last variable of gametype
        # is passed to it in the game logic loop where it calls update and returns the result of that function
        self.games = games()
        # pass games all constants we use 
        self.games.onColor = self.onColor
        self.games.offColor = self.offColor
        # init game type, could probably be a menu where comobs of keys start a game
        self.gameType = 'neighborGame'
        # gives boardState access to the theBoard and patternSize arg passed from init 
        self.theBoard = theBoard
        self.games.theBoard = theBoard
        self.boardSize = len(self.theBoard)
        #
        #
        self.previoustimePressed = None
        self.timePressed = None
        self.previousButtonPressed = None
        #
        #
    def debounce(self):#first press will always be smaller then second
        #sleep(0.195)
        currentTime = time()
        timebetween =  currentTime - self.timePressed
        print(timebetween)
        if timebetween <= 0.2:
            return False # return false str if true
        else:
            return True # else return true, the time between pressed is valid

    def checkWin(self):
        if self.onColor not in self.theBoard:
           return True

    # random pattern game init
    def simMyBoard(self,buttonPressed):
    # get a copy of the board to modify and return
    
        for buttonValue in range(self.boardSize):
            # if button value == buttonPressed
            if buttonValue == buttonPressed:
                self.doGameLogic(buttonPressed)
            

    def clearArray(self):
        self.theBoard = [self.offColor] * self.boardSize


    # add an optional argument for simulation which sets event = to a normal int value not .numbers
    # takes theboard and "event" or pressed button as an argument,
    # and returns the updated board state
    def doGameLogic(self, event, sim=True):
        
        # get a button time stamp to beckeck by debouncing
        self.timePressed = time()
        # if optional sim flag event is just an int otherwise its obj with an int
        if sim:
            pressedButton = event
        else:
            pressedButton = event.number
        #
        #store the event to the games object as it needed to construct the arg that class the game function
        self.games.event = pressedButton
        #
        # check the time between button presses is >= prev press time threshold 
        sleep(0.02)
        if self.debounce():
            print("passed Debounce event with number:",pressedButton)
            #
            if not pressedButton == self.previousButtonPressed:
                print("prev pressed check passed with:",self.previousButtonPressed)
                self.previousButtonPressed = pressedButton
                #
                #check if the game has be won
                if self.checkWin():
                    print("win condition met logically")
                    for i in range(16):
                        self.theBoard[i] = self.GREEN
                #
                # applythe gamtype to the button
                # store the game to the games object as it needed to construct the arg that class the game function
                else:
                    # i think this may cause a crash
                    # at this point the game argument is constructed, passing the gameType is the final step
                    self.games.game = self.gameType
                    # returning the board after update is called, and passing it to our board
                    self.theBoard = self.games.update()
        
                    
if __name__ == '__main__':
    boardDriver = boardState([(0,0,0)]*16)
    boardDriver.theBoard[randrange(0,15)] = boardDriver.onColor
    x = 0
    while True:
        if x >= 15:
            x = 0
        if x == 10:
            boardDriver.simMyBoard(randrange(x,15))
        elif x == 0:
            boardDriver.simMyBoard(randrange(x,5))
        else:
            boardDriver.simMyBoard(randrange(x,15))
        print(boardDriver.theBoard)
        # if you press the nuke button reset
        if boardDriver.GREEN in boardDriver.theBoard:
            break
        x += 1
        sleep(0.02)
    

