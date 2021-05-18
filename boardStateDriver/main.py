import boardStateDriver, tests
x = boardStateDriver.boardState([0]*16, 7)
pattern = x.randomArray()
print(pattern)
for i in range(len(x.theBoard)):
    x.theBoard = tests.simMyBoard(pattern, i, x.theBoard)
print(x.theBoard, "before reset")
x.theBoard = x.clearArray()
print(x.theBoard)