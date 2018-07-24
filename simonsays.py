import RPi.GPIO as GPIO
import LEDRGB as LED
import time
import random
#this script demonstrates looping through a list
#breadboard setup
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#assign pin number for Passive Buzzer; pin 32 = GPIO 12

buzz_pin = 32

#set Passive Buzzer pin's mode as outpu
GPIO.setup(buzz_pin,GPIO.OUT)


Buzz = GPIO.PWM(buzz_pin,1000)
colors = ['R','G','B','Y']
frequencies = [220, 440, 880, 1760]

R_pin = 11
G_pin = 12
B_pin = 13
colorlist = []
LED.setup(R_pin, G_pin, B_pin)
def append_list():
	while True:
		n = random.randint(0,3)
		colorlist.append(n)
		for i in colorlist:
			LED.setColor(colors[i])
			Buzz.ChangeFrequency(frequencies[i])
			Buzz.start(10)
			time.sleep(0.5)
			LED.noColor()
			Buzz.stop()
			time.sleep(0.5)

if __name__ == '__main__':
	try:
		append_list()
	except KeyboardInterrupt:
		print "Goodbye"
		LED.destroy()
		Buzz.stop()





