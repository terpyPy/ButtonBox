import boardStateDriver
import time
from adafruit_seesaw.neopixel import NeoPixel
import board
from board import SCL, SDA
import digitalio
import busio
from adafruit_neotrellis.neotrellis import NeoTrellis
from random import randrange

# create the i2c object for the trellis
i2c_bus = busio.I2C(SCL, SDA)   

# create the trellis
theTrellis = NeoTrellis(i2c_bus)

button_pin = board.D6

button = digitalio.DigitalInOut(button_pin)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

# ALWAYS PASS x.theBoard TO ITS SELF WHEN CHANGING STATE!!!!!!!!!!!!
boardDriver = boardStateDriver.boardState([(0,0,0)]*16)

for i in range(16):
    theTrellis.activate_key(i, NeoTrellis.EDGE_RISING)
    theTrellis.callbacks[i] = boardDriver.gameLogic

# ALWAYS PASS x.theBoard TO ITS SELF WHEN CHANGING STATE!!!!!!!!!!!!
boardDriver.theBoard[randrange(0,15)] = boardDriver.onColor

for i in range(16):
    theTrellis.pixels[i] = boardDriver.OFF

while True:
    time.sleep(0.02)
    # if you press the nuke button reset
    if not button.value:
        boardDriver.clearArray()# ALWAYS PASS x.theBoard TO ITS SELF WHEN CHANGING STATE!!!!!!!!!!!!
        boardDriver.theBoard[randrange(0,15)] = boardDriver.onColor
    else:
        for i in range(len(boardDriver.theBoard)):
            theTrellis.pixels[i] = boardDriver.theBoard[i]
    theTrellis.sync()
