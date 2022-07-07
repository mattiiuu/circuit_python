import time
from adafruit_circuitplayground import cp

# set tapped to true if tapped once
cp.detect_taps = 1

import random


answerbank = ['It is certain.', 'It is decidedly so.', 'Without a doubt.', 'Yes – definitely.', 'You may rely on it.', 'As I see it, yes.', 'Most likely.' 'Outlook good.', 'Yes.', 'Signs point to yes.', 'Reply hazy, try again.', 'Ask again later.', 'Better not tell you now.', 'Cannot predict now.', 'Concentrate and ask again.', 'Dont count on it.', 'My reply is no.', 'My sources say no.', 'Outlook not so good.', 'Very doubtful.']


random_answer = random.choice(answerbank)
while True:
    if cp.tapped==True:
        for	i in range (3):
            for i in range (0,10):
                cp.pixels[i] = ((255,0,255))
                time.sleep(0.3)
            for i in range (0,10):
                cp.pixels[i] = ((0,0,0))
                time.sleep(0.3)
        print(random_answer)

        


