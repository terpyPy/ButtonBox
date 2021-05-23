import boardStateDriver
from time import sleep
from adafruit_seesaw.neopixel import NeoPixel
import board
from board import SCL, SDA
import digitalio
import busio
from adafruit_neotrellis.neotrellis import NeoTrellis

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

boardDriver.theBoard = boardDriver.setRandom()

while True:
    sleep(0.02)
    # if you press the nuke button reset
    if not button.value:
        boardDriver.previousButtonPressed = None
        boardDriver.clearArray()
        boardDriver.setRandom()
    else:
        for i in range(16):
            theTrellis.pixels[i] = boardDriver.theBoard[i]
    theTrellis.sync()
