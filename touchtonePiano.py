import board
from adafruit_circuitplayground import cp

while True:
    if cp.touch_A1:
        cp.play_tone(262,1) #note c
    elif cp.touch_A2:
        cp.play_tone(294,1) # note d
    elif cp.touch_A3:
        cp.play_tone(330,1) # note e
    elif cp.touch_A4:
        cp.play_tone(349,1) #note f
    elif cp.touch_A5:
        cp.play_tone(392,1) #note g
    elif cp.touch_A6:
        cp.play_tone(440,1)
    elif cp.touch_A7:
        cp.play_tone(494,1)
