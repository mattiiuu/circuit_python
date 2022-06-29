import board
import neopixel
import time 

led = neopixel.NeoPixel(board.NEOPIXEL, 10)

led.brightness = 0.1

while True:
    for i in range(10):
        time.sleep(0.3)
        led[i] = (255, 0, 0)

        time.sleep(0.3)
    for i in range(9, -1, -1):
        led[i] = (253,10, 30)
        
    
        time.sleep(0.3)
    for i in range (10):
        led[i] = (66,165,245)
        
        led[i] = (66,165,245)
