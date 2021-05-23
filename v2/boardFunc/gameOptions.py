import boardFunc
class games:
    def __init__(self,game=None, theBoard=None ,event=None, onColor=None, offColor=None):
        self.game = game
        self.theBoard =theBoard
        self.event = event
        self.onColor = onColor
        self.offColor = offColor
        
    def update(self):
        if self.game != None:
            gameList = {'neighborGame':boardFunc.neighborGame(self.theBoard ,self.event, self.onColor, self.offColor) if self.game == 'neighborGame'else None}
            return  gameList[self.game]