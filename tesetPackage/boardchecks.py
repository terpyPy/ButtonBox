def reset(theBoard):
    # get a copy of the board to modify and return
    newBoard = theBoard

    for boardIndex, val  in enumerate(newBoard): # enumerate gets the index and the value for each iteration of loop
        # if the value of boardIndex is == 1
        if val == 1:
            print('_in_boardchecks____reset', val, boardIndex, 
                    'successful reset')
            newBoard[boardIndex] = 0
        # else dont reset value, skip it and print debug
        else:
            print('_in_boardchecks____reset', val, boardIndex, 
                    'Off position found in reset!!!!!!')
    # return the Board modified copy 
    return newBoard

# board simulation works with test case:
# if run as a standalone script instead of imported run the test case
# if __name__ == "__main__":   
#     gamePattern  = [2,3,5,10] # test case comment out before unit test
#     gameBoard = [0] * 16 # test case comment out before unit test
#     for j in range(len(gameBoard)):
#         gameBoard = checkBoard(gamePattern, j, gameBoard)
#     print(gameBoard)
#     gameBoard = reset(gameBoard)
#     print(gameBoard)