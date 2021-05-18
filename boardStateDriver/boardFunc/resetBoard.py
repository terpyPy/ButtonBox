def resetBoard(theBoard):
    # get a copy of the board to modify and return
    newBoard = theBoard

    for boardIndex, val  in enumerate(newBoard): # enumerate gets the index and the value for each iteration of loop
        # if the value of boardIndex is == 1
        if val != 0:
            print('_in_boardchecks____reset', val, boardIndex, 
                    'successful reset')
            newBoard[boardIndex] = 0
        # else dont reset value, skip it and print debug
        else:
            print('_in_boardchecks____reset', val, boardIndex, 
                    'Off position found in reset!!!!!!')
    # return the Board modified copy
     
    return newBoard


if __name__ == "__main__":   
    i = [1] * 16
    print('script run as __main__ test block')
    print('all on array: ', i)
    resetBoard(i)
    print('after reset test: ', i)   