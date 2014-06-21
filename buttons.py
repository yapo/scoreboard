import pygame, termios, fcntl, sys, os
import RPi.GPIO as GPIO



def enable_button_events(self):
	pass

def disable_button_events(self):
	pass

def button_1_callback(self):
	print("Button 1 pressed")

def button_2_callback(self):
	print("Button 2 pressed")

def quit():
	GPIO.cleanup()
	looping = False


GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(24, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.add_event_detect(23, GPIO.RISING)
GPIO.add_event_detect(24, GPIO.RISING)
GPIO.add_event_callback(23, button_1_callback)
GPIO.add_event_callback(24, button_2_callback)


options =	{ 'q': quit }
looping = True
fd = sys.stdin.fileno()
oldterm = termios.tcgetattr(fd)
newattr = termios.tcgetattr(fd)
newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
termios.tcsetattr(fd, termios.TCSANOW, newattr)
oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK)
try:
	while looping:
		try:
			c = sys.stdin.read(1)
			if c in options:
				options[c]()
		except IOError: pass
finally:
	termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
	fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)






