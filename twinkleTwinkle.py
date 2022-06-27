from adafruit_circuitplayground import cp


noteC = 262
noteD = 294
noteE = 330
noteF = 349
noteG = 392
noteA = 440
noteB = 494
noteCC = 523

sounds = [noteC , noteC, noteG, noteG, noteA, noteA, noteG, noteF, noteF, noteE, noteE, noteD, noteD, noteC, noteG, noteG, noteF, noteF, noteE, noteE, noteD, noteG, noteG, noteF, noteF, noteE, noteE, noteD]

for freq in sounds:
    cp.play_tone(freq,0.5)
