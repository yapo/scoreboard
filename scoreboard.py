import pygame, termios, fcntl, sys, os

class example(object):

	def __init__(self):
		pygame.mixer.pre_init(44100, -16, 2, 2048)
		pygame.init()
		self.options =	{
					'q': self.quit,
					'1': self.play1,
					'2': self.play2,
					'p': self.pause
				}
		self.looping = True
		self.is_pause = False
		self.audio_init()

	def audio_init(self):
		pygame.mixer.music.set_volume(0.1)
		pygame.mixer.music.load('sounds/crowd.mp3')
		self.load_audio_files()
		pygame.mixer.music.play(-1)

	def load_audio_files(self):
		self.audio = {	"ding": pygame.mixer.Sound('sounds/ding.mp3'),
				"firstBlood": pygame.mixer.Sound('sounds/1-first-blood.mp3'),
				"dominating": pygame.mixer.Sound('sounds/2-dominating.mp3'),
				"unstoppable": pygame.mixer.Sound('sounds/unstoppable.mp3'),
				"wickedSick": pygame.mixer.Sound('sounds/whicked-sick.mp3'),
				"triple": pygame.mixer.Sound('sounds/3-triple.mp3'),
				"super": pygame.mixer.Sound('sounds/4-super.mp3'),
				"hyper": pygame.mixer.Sound('sounds/5-hyper.mp3'),
				"brutal": pygame.mixer.Sound('sounds/6-brutal.mp3'),
				"master": pygame.mixer.Sound('sounds/7-master.mp3'),
				"awesome": pygame.mixer.Sound('sounds/8-awesome.mp3'),
				"blaster": pygame.mixer.Sound('sounds/9-blaster.mp3'),
				"monster": pygame.mixer.Sound('sounds/10-monster.mp3'),
				"comboBreaker": pygame.mixer.Sound('sounds/combo-breaker.mp3'),
				"crowd": pygame.mixer.Sound('sounds/crowd.mp3'),
				"excellent": pygame.mixer.Sound('sounds/excellent.mp3'),
				"finishHim": pygame.mixer.Sound('sounds/finish-him.mp3'),
				"humiliation": pygame.mixer.Sound('sounds/humiliation.mp3'),
				"superb": pygame.mixer.Sound('sounds/superb.mp3'),
				"supremeVictory": pygame.mixer.Sound('sounds/supreme-victory.mp3'),
				"thatWasPathetic": pygame.mixer.Sound('sounds/that-was-pathetic.mp3'),
				"danger": pygame.mixer.Sound('sounds/danger.mp3'),
				"wellDone": pygame.mixer.Sound('sounds/well-done.mp3'),
				"winner": pygame.mixer.Sound('sounds/winner.mp3'),
				"youllNeverWin": pygame.mixer.Sound('sounds/youll-never-win.mp3'),
				"victory": pygame.mixer.Sound('sounds/victory.mp3')	}

	def quit(self):
		print "quiting"
		self.looping = False
		pygame.mixer.quit()

	def pause(self):
		if self.is_pause:
			print 'unpausing'
			pygame.mixer.music.unpause()
		else:
			print 'pausing'
			pygame.mixer.music.pause()
		self.is_pause = not self.is_pause

	def play1(self):
		self.audio["victory"].play()

	def play2(self):
		self.audio["winner"].play()

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
					if c in self.options:
						self.options[c]()
				except IOError: pass
		finally:
			termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
			fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)


example().run()
