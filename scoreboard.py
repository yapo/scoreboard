import termios, fcntl, sys, os

class example(object):

	def __init__(self):
		self.options = {'q': quit}
		self.looping = True
		print "constructor"

	def quit(self):
		print "quiting"
		self.looping = False

	def run(self):
		print "starting"
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
					c = repr(c)
					print "Got character {}" 
					if c in self.options:
						self.options[c]()
				except IOError: pass
		finally:
			termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
			fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)


example().run()
