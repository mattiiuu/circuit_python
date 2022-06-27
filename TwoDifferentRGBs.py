import board
import neopixel

from digitalio import DigitalInOut, Direction, Pull


led = neopixel.NeoPixel(board.NEOPIXEL, 10)
led.direction = Direction.OUTPUT


switch = DigitalInOut(board.SLIDE_SWITCH)
switch.direction = Direction.INPUT
switch.pull = Pull.UP

led.brightness = 0.1
while True:
    if (switch.value==True):
        led[9] = (255,0,0)
        led[5] = (0,0,0)
    else:
        led[5] = (0,255,0)
        led[9] = (0,0,0)
