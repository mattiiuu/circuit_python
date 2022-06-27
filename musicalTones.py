from adafruit_circuitplayground import cp


noteC = 262
noteD = 294
noteE = 330
noteF = 349
noteG = 392
noteA = 440
noteB = 494
noteCC = 523

sounds = [262 , 294, 330, 349, 392, 440, 494, 523]

for freq in sounds:
    cp.play_tone(freq,1)
