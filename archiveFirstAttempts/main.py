#Authors Hunter Hannula, Cameron Kerley

import time
import random
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

# some color definitions
OFF = (0, 0, 0)
RED = (25, 0, 0)
YELLOW = (25, 15, 0)
GREEN = (0, 25, 0)
CYAN = (0, 25, 25)
BLUE = (0, 0, 25)
PURPLE = (18, 0, 25)
WHITE = (127, 127, 127)

animColor = WHITE
rightColor = GREEN
wrongColor = RED

COLORS = [RED, YELLOW, GREEN, CYAN, BLUE, PURPLE]
gamePattern  = [0,3,5,10]

showReset = True
guessesLeft = 3
prevWrongAnswers = [None]

# this will be called when button events are received

def reset():
    global guessesLeft
    global prevWrongAnswers
    for j in range(16):
                trellis.pixels[j] = animColor
                time.sleep(.05)
                trellis.pixels[j] = OFF
                time.sleep(.05)
                showReset = False
    guessesLeft = 3
    prevWrongAnswers.clear()

def blink(event):
    global guessesLeft
    global prevWrongAnswers
    # turn the LED on when a rising edge is detected
    if event.edge == NeoTrellis.EDGE_RISING:
        print("rem guess",guessesLeft)
        print("event number",event.number)
        print("prev wrong",prevWrongAnswers)
        print("cur button is in prevWrong",event.number not in prevWrongAnswers)
        if button.value:
            # a button was pushed, now check if it is in the pattern
            if event.number in gamePattern:
                # button was correct, set to appropriate color
                trellis.pixels[event.number] = rightColor
            if (event.number in prevWrongAnswers and prevWrongAnswers[0] == None):
                # wrong answer already input, do nothing
                pass
            else:
               # button was incorrect, set to appropriate color
                trellis.pixels[event.number] = wrongColor
                prevWrongAnswers.append(event.number)
                guessesLeft -= 1
                if guessesLeft == 0:
                    reset()
                    #showReset = True

    # do falling edge (todo)
    elif event.edge == NeoTrellis.EDGE_FALLING:
        #trellis.pixels[event.number] = random.choice([RED, YELLOW, GREEN, CYAN, BLUE, PURPLE])
        pass


for i in range(16):
    # activate rising edge events on all keys
    trellis.activate_key(i, NeoTrellis.EDGE_RISING)
    # activate falling edge events on all keys
    trellis.activate_key(i, NeoTrellis.EDGE_FALLING)
    # set all keys to trigger the blink callback
    trellis.callbacks[i] = blink

    # cycle the LEDs on startup
    trellis.pixels[i] = animColor
    time.sleep(.05)

for i in range(16):
    trellis.pixels[i] = OFF
    time.sleep(.05)

while True:
    # call the sync function call any triggered callbacks
    trellis.sync()
    # the trellis can only be read every 17 millisecons or so
    time.sleep(.02)
