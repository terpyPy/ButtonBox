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
button.pull = digitalio.Pull.DOWN

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

boardArray = [OFF]*16


def redrawBoard(colorArray):
    
    #global boardArray
    off = colorArray[6]
    trellis.pixels[0] = colorArray[randrange(0,5)]
    time.sleep(.05)
    for i in range(len(boardArray)):
        print("I:",i)
        if (boardArray[i] == off) and (i < 16) :
            trellis.pixels[i] = colorArray[randrange(0,5)]
            time.sleep(.05)
def blink(event):
    # turn the LED on when a rising edge is detected
    if event.edge == NeoTrellis.EDGE_RISING:
        if button.value:
            print("try redraw board")
            
    elif event.edge == NeoTrellis.EDGE_FALLING:
        print("falling")
        redrawBoard(COLORS)
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
    # call the sync function call any triggered callbacks
    trellis.sync()
    # try:
    #     trellis.sync()
    # except OSError:
    #     print("THIS IS PROBLEM")
    # the trellis can only be read every 17 millisecons or so
    time.sleep(.02)