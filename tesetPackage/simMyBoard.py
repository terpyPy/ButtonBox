
def checkBoard(pattern, buttonPressed, boardArray):
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
    gamePattern  = [2,3,5,10] # test case comment out before unit test
    gameBoard = [0] * 16 # test case comment out before unit test      
    for j in range(16):
        checkBoard(gamePattern, j, gameBoard)
    print(gameBoard)