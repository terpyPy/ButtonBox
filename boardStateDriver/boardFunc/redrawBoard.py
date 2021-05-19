def redrawBoard(theBoard, event):
    neighbors = {0:(1,4,5),1:(0,2,4,5,6),2:(1,3,5,6,7),3:(2,6,7),
            4:(0,1,5,9,8),5:(0,1,2,4,6,8,9,10),6:(1,2,3,5,7,9,10,11),7:(3,2,6,10,11),8:(4,5,9,12,13),
            9:(5,4,6,8,10,12,13,14),10:(5,6,7,9,11,13,14,15),11:(6,7,10,14,15),12:(8,9,13),13:(8,9,10,12,14),
            14:(9,10,11,13,15),15:(10,11,14)}
    keyPressed = event.number
    newBoard = theBoard
    newBoard[keyPressed] = 0
    for i in range(len(neighbors[keyPressed])):
        newBoard[neighbors[keyPressed][i]] = 1
    print(event.number)
    return newBoard