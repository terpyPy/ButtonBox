def gameLogic(theBoard, event, onColor, offColor):
    #
    # dictionary that contains button numbers and their corresponding direct neighbor cells (does not include corner neighbors)
    neighbors = { 0:(4, 1),1:(5, 2, 0),2:(1, 6, 3),3:(7, 2),4:(0, 8, 5),5:(1, 4, 9, 6),6:(2,5,10,7),7:(6, 3,11),8:(12, 9,4),9:(5,8,13,10),10:(6,9,14,11),11:(7,10,15),12:(8,13),13:(12,9,14),14:(13,10,15),15:(11,14)}
    keyPressed = event.number
    newBoard = theBoard
    # turn off the pressed key
    newBoard[keyPressed] = offColor
    # do this loop i times, where i is the number of neighbors for the pressed button 
    for i in range(len(neighbors[keyPressed])):
        # invert the value of this neighbor of the pressed button
        if theBoard[neighbors[keyPressed][i]] == offColor:
            newBoard[neighbors[keyPressed][i]] = onColor
        elif theBoard[neighbors[keyPressed][i]] == onColor:
            newBoard[neighbors[keyPressed][i]] = offColor
    # return the new board
    return newBoard
