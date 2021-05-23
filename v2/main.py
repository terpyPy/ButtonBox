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

boardDriver = boardStateDriver.boardState([(0,0,0)]*16)

for i in range(16):
    theTrellis.activate_key(i, NeoTrellis.EDGE_RISING)
    theTrellis.callbacks[i] = boardDriver.doGameLogic

boardDriver.theBoard[randrange(0,15)] = boardDriver.onColor
x = 0
while True:
    if x >= 16:
        x = 0
    time.sleep(0.02)
    boardDriver.simMyBoard(x)
    # if you press the nuke button reset
    if not button.value:
        boardDriver.clearArray()
    else:
        for i in range(16):
            
            theTrellis.pixels[i] = boardDriver.theBoard[i]
            if boardDriver.GREEN in boardDriver.theBoard:
                boardDriver.clearArray()
                boardDriver.theBoard[randrange(0,15)] = boardDriver.onColor
    x += 1
    theTrellis.sync()
