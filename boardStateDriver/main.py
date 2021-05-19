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

x = boardStateDriver.boardState([0]*16)

for i in range(16):
    # activate rising edge events on all keys
    trellis.activate_key(i, NeoTrellis.EDGE_RISING)
    # activate falling edge events on all keys
    trellis.activate_key(i, NeoTrellis.EDGE_FALLING)
    # set all keys to trigger the blink callback
    trellis.callbacks[i] = x.redrawBoard

for i in range(16):
    trellis.pixels[i] = x.OFF

x.theBoard[randrange(0,15)] = 1

while True:
    if not button.value:
        x.theBoard = x.clearArray()
        time.sleep(0.02)
    else:
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