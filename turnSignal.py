from adafruit_circuitplayground import cp
import time

left_light = False
right_light = False


while True:
    if cp.button_a==True:
        while(cp.button_a==True):
            pass
        # click detected
        left_light = not left_light
        print("left light:", left_light)
        if left_light:
            right_light = False
        if left_light==True:
            for i in range(5):
                cp.pixels[i] =(228,20,10)
                time.sleep(0.1)
            for i in range(5): 
                cp.pixels[i] =(0,0,0)


    if cp.button_b==True:
        while(cp.button_b==True):
            pass
        #click detected
        right_light = not right_light
        print("right light:" , right_light)
        if right_light:
            left_light = False
        if right_light == True:
            for i in range(9,4, -1):
                cp.pixels[i]= (228, 20, 10)
                time.sleep(0.1)
            for i in range (9,4,-1):
                cp.pixels[i] = (0,0,0)
            
