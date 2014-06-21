import pygame, termios, fcntl, sys, os
from lib import config, audio_handler, button_handler

class scoreboard():
	def __init__(self):
		print "constructor"
		self.config = config.config()
		self.audio_handler = audio_handler.audio_handler(self.config)
		self.button_handler = button_handler.button_handler(self.config)
		self.looping = True
		self.options =	{ 'q': self.quit }
		self.button_handler.add_handler('a', self.a_event_handler)
		self.button_handler.add_handler('b', self.b_event_handler)
		self.button_handler.add_handler('c', self.c_event_handler)

	def terminate(self):
		self.audio_handler.terminate()
		self.button_handler.terminate()

	def quit(self):
		print "quiting"
		self.looping = False

	def a_event_handler(self):
		print 'goal player 1'

	def b_event_handler(self):
		print 'goal player 2'

	def c_event_handler(self):
		print 'restart game'

	def run(self):
		print "running"
		fd = sys.stdin.fileno()
		oldterm = termios.tcgetattr(fd)
		newattr = termios.tcgetattr(fd)
		newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
		termios.tcsetattr(fd, termios.TCSANOW, newattr)
		oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
		fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK)
		try:
			while self.looping:
				try:
					c = sys.stdin.read(1)
					if c in self.options:
						self.options[c]()
				except IOError: pass
		finally:
			self.audio_handler.terminate()
			self.button_handler.terminate()
			termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
			fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)


scoreboard().run()

		
