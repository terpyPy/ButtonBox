# play sudo game as simulation of the board and events, 
# used to to prove the board state logic should be valid at the abstaction layer interface that is the boardStateDriver
def simMyBoard(pattern, buttonPressed, boardArray):
    # get a copy of the board to modify and return
    newBoard = boardArray
    for buttonValue in range(len(boardArray)):
        # if button value == buttonPressed
        if buttonValue == buttonPressed:
            if buttonPressed in pattern:
                newBoard[buttonValue] = 1
    return newBoard

# if run as a standalone script instead of imported run the test case    
if __name__ == "__main__": 
    # test case simulation
    print('test cast is being simulated')
    gamePattern  = [2,3,5,10] 
    gameBoard = [0] * 16 
    for j in range(16):
        simMyBoard(gamePattern, j, gameBoard)
    print(gameBoard)