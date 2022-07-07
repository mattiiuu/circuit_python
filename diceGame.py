from adafruit_circuitplayground import cp
import random
import time



while True:
    if cp.button_a==True:
        while(cp.button_a==True):
            pass
        random1 = random.randint(0,5)
        for i in range(random1):
            cp.pixels[i] = ((255,0,0))
        print(random1)
    elif cp.button_b == True:
        while(cp.button_b == True):
            pass
        random2 = random.randint(5,11)
        for i in range (5, random2):
            cp.pixels[i] = (0,0,255)
        print(random2)
