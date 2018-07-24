import RPi.GPIO as GPIO
import LEDRGB as LED
import time
import random
#this script demonstrates looping through a list
colors = ['R','G','B','Y']
R_pin = 11
G_pin = 12
B_pin = 13
LED.setup(R_pin, G_pin, B_pin)
def append_list():
	while True:
		n = random.randint(0,3)
		LED.setColor(colors[n])
		time.sleep(1)

if __name__ == '__main__':
	try:
		append_list()
	except KeyboardInterrupt:
		print "Goodbye"
		LED.destroy()

