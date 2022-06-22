import board
from digitalio import DigitalInOut, Direction


led = DigitalInOut(board.LED)
led.direction = Direction.OUTPUT


while True:
    led.value = True
