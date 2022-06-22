from adafruit_circuitplayground import cp

while True:
	    if cp.button_a == True:
	        cp.play_file("smb_powerup.wav")
	    elif cp.button_b == True:
	        cp.play_file("smb_mariodie.wav")
