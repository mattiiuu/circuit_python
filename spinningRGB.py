import board
import neopixel
import time 

led = neopixel.NeoPixel(board.NEOPIXEL, 10)

led.brightness = 0.1

while True:
    for i in range(10):
        led[i] = (52, 210, 235)
        time.sleep(0.08)
        #led[i] = (0,0,0)
    for i in range(10):
        led[i] = (122, 171,62)
        time.sleep(0.08)
        #led[i] = (0,0,0)
    for i in range (10):
        led[i] = (232,78,12)
        time.sleep(0.08)
        #led[i] = (0,0,0)
