def resetBoard(theBoard, offColor, onColor):
    # get a copy of the board to modify and return
    newBoard = theBoard

    for boardIndex, val  in enumerate(newBoard): # enumerate gets the index and the value for each iteration of loop
        # if the value of boardIndex is not 0 turn it off
        if val != offColor:
            newBoard[boardIndex] = offColor
        # else dont reset value, skip it 
        else:
            pass
    # return the Board modified copy
    return newBoard
