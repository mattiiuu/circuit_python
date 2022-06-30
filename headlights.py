import board
import analogio
import time
import neopixel
 
light = analogio.AnalogIn(board.LIGHT)
led = neopixel.NeoPixel(board.NEOPIXEL, 10)


while True:
    print(light.value)
    if light.value < 3000:
        led[3] = (255,255,255)
        led[4] = (255,255,255)
        led[5] = (255, 255, 255)
        led[6] = (255,255,255)
        led[7] = (255, 255, 255)
        led [8] = (255,255,255)
        led[9] = (255,255,255)
    elif light.value >= 3000:
        led[3] = (0,0,0)
        led[4] = (0,0,0)
        led[5] = (0, 0, 0)
        led[6] = (0,0,0)
        led[7] = (0, 0, 0)
        led [8] = (0,0,0)
        led[9] = (0,0,0)
    time.sleep(1)


