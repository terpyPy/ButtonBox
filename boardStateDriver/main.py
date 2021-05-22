import boardStateDriver, tests
import time
from random import randrange
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
# ALWAYS PASS x.theBoard TO ITS SELF WHEN CHANGING STATE!!!!!!!!!!!!
x = boardStateDriver.boardState([0]*16)

for i in range(16):
    # activate rising edge events on all keys
    trellis.activate_key(i, NeoTrellis.EDGE_RISING)
    # activate falling edge events on all keys
    #trellis.activate_key(i, NeoTrellis.EDGE_FALLING)
    # set all keys to trigger the blink callback
    trellis.callbacks[i] = x.redrawBoard

for i in range(16):
    trellis.pixels[i] = x.OFF

# ALWAYS PASS x.theBoard TO ITS SELF WHEN CHANGING STATE!!!!!!!!!!!!
x.theBoard[randrange(0,15)] = 1

while True:
    # if you press the nuke button reset
    if not button.value:
        x.theBoard = x.clearArray()# ALWAYS PASS x.theBoard TO ITS SELF WHEN CHANGING STATE!!!!!!!!!!!!
        time.sleep(0.02)
        x.theBoard[randrange(0,15)] = 1
        time.sleep(0.02)
    else:
        # for the len of the virtual board check the logical state of each button, 0 or 1
        # and set it to the physical board,  WHITE or OFF
        for i in range(16):
            if x.theBoard[i] == 1:
                trellis.pixels[i] = x.WHITE
            elif x.theBoard[i] == 0:
                trellis.pixels[i] = x.OFF
        trellis.sync()
        time.sleep(0.02)

# print(x.theBoard, "before reset")
# x.theBoard = x.clearArray()
# print(x.theBoard)
