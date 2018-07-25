import RPi.GPIO as GPIO
import LEDRGB as LED
import time
import random
from getpass import getpass
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
color_s = []

LED.setup(R_pin, G_pin, B_pin)

def validateGuess(color, guess):
	if color == guess.upper():
		print "Correct!"
	else:
		print "You lose!"
		print "It was",color,"and you guessed",guess.upper()
		print "You were on level",len(color_s)
		LED.destroy()
		Buzz.stop()
		exit()
		
	
def append_list():
	while True:
		n = random.randint(0,3)
		colorlist.append(n)
		color_s.append(colors[n])
		for i in colorlist:
			LED.setColor(colors[i])
			Buzz.ChangeFrequency(frequencies[i])
			Buzz.start(10)
			time.sleep(0.5)
			LED.noColor()
			Buzz.stop()
			time.sleep(0.5)
		guess = getpass("Guess the color sequence: ")
		colorString = ''.join(color_s)
		validateGuess(colorString, guess)
if __name__ == '__main__':
	try:
		append_list()
	except KeyboardInterrupt:
		print "Goodbye"
		LED.destroy()
		Buzz.stop()





