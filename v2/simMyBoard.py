import boardStateDriver, random
import time
gameBoard = [(0,0,0)]*16
theboard = boardStateDriver.boardState(gameBoard)
# play sudo game as simulation of the board and events, 
# used to to prove the board state logic should be valid at the abstaction layer interface that is the boardStateDriver
def simMyBoard(buttonPressed):
    # get a copy of the board to modify and return
    
    for buttonValue in range(len(theboard.theBoard)):
        # if button value == buttonPressed
        if buttonValue == buttonPressed:
           theboard.doGameLogic(buttonPressed,sim=True)
            
            

# if run as a standalone script instead of imported run the test case    
if __name__ == "__main__": 
    # test case simulation
    print('test cast is being simulated')
    i = 0
    theboard.theBoard[random.randrange(0,15)] = theboard.onColor
    while True:
        i += 1
        print(i)
        simMyBoard(random.randrange(15))
        print(theboard.theBoard)
        time.sleep(0.01)
        simMyBoard(random.randrange(7))
        if theboard.GREEN in theboard.theBoard:
            break