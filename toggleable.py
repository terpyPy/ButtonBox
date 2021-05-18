#Authors Hunter Hannula, Cameron Kerley

import time
from random import randrange # possibly remove, if we use random we should write a seprate module for those functions
from adafruit_seesaw.neopixel import NeoPixel
import board
from board import SCL, SDA
import digitalio
import busio
from adafruit_neotrellis.neotrellis import NeoTrellis

# create the i2c object for the trellis
i2c_bus = busio.I2C(SCL, SDA)

# create the trellis
trellis = NeoTrellis(i2c_bus)

button_pin = board.D6

button = digitalio.DigitalInOut(button_pin)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

# hack to allow me to demo both games on one run and switch between them
doGuessingGame = True

# some color definitions
OFF = (0, 0, 0)
RED = (25, 0, 0)
YELLOW = (25, 15, 0)
GREEN = (0, 25, 0)
CYAN = (0, 25, 25)
BLUE = (0, 0, 25)
PURPLE = (18, 0, 25)
WHITE = (127, 127, 127)
COLORS = [RED, YELLOW, GREEN, CYAN, BLUE, PURPLE, OFF]

ANIM_COLOR = WHITE
RIGHT_COLOR = GREEN
WRONG_COLOR = RED

guessesLeft = 3
#initialize blank board array
boardArray = [OFF]*16
#set pattern to a snakey thing
gamePattern = [0,3,5,6,9,10,12,15]
prevWrongAnswers = [None]
prevRightAnswers = [None]
# to port this game to my pkg we need too create a method that translates the pressed button to the game driver object thats our interfacewith the layer
# after that change the logic so that it check the array game board representation from the driver and then start adding the extra reset and re draw fetuers needed
# will also fixsome gloabel scope stuff puttin gamePattern boardArray guessesLeft prevWrongAnswers prevRightAnswers and all the constants for colorin the gameDriverObject
#   -----Cameron, had to write this down came to me out of the blue watchin videos
def resetBoard():
    global guessesLeft
    for i in range(len(boardArray)):
        trellis.pixels[i] = OFF
    if doGuessingGame:
        guessesLeft = 3
        gamePattern  = [0,3,5,6,9,10,12,15]
        print(gamePattern)
        prevWrongAnswers.clear()
        prevRightAnswers.clear()
        prevWrongAnswers.append(None)
        prevRightAnswers.append(None)

def redrawBoard(colorArray, event):
    global guessesLeft
    if doGuessingGame:
        # name event for readability
        pressedNumber = event.number
        # a button was pushed, now check if it is in the pattern and not already inpu
        if (pressedNumber in gamePattern) and (pressedNumber not in prevRightAnswers):
            # button was correct, set to appropriate color
                trellis.pixels[pressedNumber] = RIGHT_COLOR
                prevRightAnswers.append(pressedNumber)
                if(len(prevRightAnswers)-1 >= len(gamePattern)):
                    resetBoard()
        elif pressedNumber in gamePattern and pressedNumber in prevRightAnswers:
                #pressed button was correct but already input, dont increase score, just chill
                print("hey you already did that")

        # if the pressed button is wrong and has not already been input take away a guess 
        elif (pressedNumber not in gamePattern) and (pressedNumber not in prevWrongAnswers):
            trellis.pixels[pressedNumber] = WRONG_COLOR
            prevWrongAnswers.append(pressedNumber)
            guessesLeft -= 1
            if guessesLeft == 0:
                resetBoard()

    else:
        trellis.pixels[0] = colorArray[randrange(0,5)]
        time.sleep(.05)
        for i in range(len(boardArray)):
            print("I:",i)
            if (boardArray[i] == OFF) and (i < 16) :
                trellis.pixels[i] = colorArray[randrange(0,5)]
                time.sleep(.05)
def blink(event):
    # TODO idk man
    print(event.number)
    if event.edge == NeoTrellis.EDGE_RISING:
        pass
            
    elif event.edge == NeoTrellis.EDGE_FALLING:
        print("falling")
        redrawBoard(COLORS, event)
        pass

for i in range(16):
    # activate rising edge events on all keys
    trellis.activate_key(i, NeoTrellis.EDGE_RISING)
    # activate falling edge events on all keys
    trellis.activate_key(i, NeoTrellis.EDGE_FALLING)
    # set all keys to trigger the blink callback
    trellis.callbacks[i] = blink
    time.sleep(.02)
    trellis.pixels[i] = (0, 0, 0)
    time.sleep(.02)


while True:
    # TODO debounce
    if not button.value:
        doGuessingGame = not doGuessingGame
        print("changed to",doGuessingGame)
        resetBoard()
    # call the sync function call any triggered callbacks
    trellis.sync()
    # try:
    #     trellis.sync()
    # except OSError:
    #     print("THIS IS PROBLEM")
    # the trellis can only be read every 17 millisecons or so
    time.sleep(.02)