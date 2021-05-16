from simBoard import checkBoard
gamePattern  = [2,3,5,10]
gameBoard = [0] * 16
def reset(theBoard):

    newBoard = theBoard

    for val, boardIndex in newBoard:

        if val != 0:
            print('_in_boardchecks____reset', val, boardIndex, 'successful reset')
            newBoard[boardIndex] = 0
        else:
            print('_in_boardchecks____reset', val, boardIndex, 'Off position found in reset!!!!!!')
            #return theBoard
    return newBoard
for j in range(16):
    checkBoard(gamePattern, j)
print(gameBoard)