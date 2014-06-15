import pygame, termios, fcntl, sys, os

class example(object):

	def __init__(self):
		self.options = {'q': self.quit, 'p': self.play}
		self.looping = True

	def quit(self):
		print "quiting"
		self.looping = False

	def play(self):
		print "play"
		file = 'sounds/winner.mp3'
		pygame.init()
		pygame.mixer.init()
		pygame.mixer.music.load(file)
		pygame.mixer.music.play()

	def run(self):
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
					print "Got character {}".format(repr(c))
					if c in self.options:
						self.options[c]()
				except IOError: pass
		finally:
			termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
			fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)


example().run()
