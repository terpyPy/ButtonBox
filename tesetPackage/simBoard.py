boardArray = [0] * 16
gamePattern  = [0,3,5,10]
#print(boardArray)
def checkBoard(pattern, button):
    for i in range(16):
        if i == button:
            if button in pattern:
                boardArray[i] = 1
                return boardArray
    
# for j in range(16):
#     checkBaord(gamePattern, j)
# print(boardArray)