import pygame, termios, fcntl, sys, os

class example(object):

	def __init__(self):
		pygame.mixer.pre_init(44100, -16, 2, 2048)
		pygame.init()
		self.options =	{
					'q': self.quit,
					'p': self.pause,
					'1': self.play1,
					'2': self.play2,
					'3': self.play3,
					'4': self.play4,
				}
		self.looping = True
		self.is_pause = False
		self.audio_init()

	def audio_init(self):
		pygame.mixer.music.set_volume(0.1)
		pygame.mixer.music.load('sounds/crowd.ogg')
		self.load_audio_files()
		pygame.mixer.music.play(-1)

	def load_audio_files(self):
		self.channels= {
				"ding": pygame.mixer.Channel(1),
				"firstBlood": pygame.mixer.Channel(2),
				"dominating": pygame.mixer.Channel(3),
				"unstoppable": pygame.mixer.Channel(4),
				"wickedSick": pygame.mixer.Channel(5),
				"triple": pygame.mixer.Channel(6),
				"super": pygame.mixer.Channel(7),
				# "hyper": pygame.mixer.Channel(8),
				# "brutal": pygame.mixer.Channel(9),
				# "master": pygame.mixer.Channel(10),
				# "awesome": pygame.mixer.Channel(11),
				# "blaster": pygame.mixer.Channel(12),
				# "monster": pygame.mixer.Channel(13),
				# "comboBreaker": pygame.mixer.Channel(14),
				# "crowd": pygame.mixer.Channel(15),
				# "excellent": pygame.mixer.Channel(16),
				# "finishHim": pygame.mixer.Channel(17),
				# "humiliation": pygame.mixer.Channel(18),
				# "superb": pygame.mixer.Channel(19),
				# "supremeVictory": pygame.mixer.Channel(20),
				# "thatWasPathetic": pygame.mixer.Channel(21),
				# "danger": pygame.mixer.Channel(22),
				# "wellDone": pygame.mixer.Channel(23),
				# "winner": pygame.mixer.Channel(24),
				# "youllNeverWin": pygame.mixer.Channel(25),
				# "victory": pygame.mixer.Channel(26)
				}
		self.audios = {
				"ding": pygame.mixer.Sound('sounds/ding.ogg'),
				"firstBlood": pygame.mixer.Sound('sounds/1-first-blood.ogg'),
				"dominating": pygame.mixer.Sound('sounds/2-dominating.ogg'),
				"unstoppable": pygame.mixer.Sound('sounds/unstoppable.ogg'),
				"wickedSick": pygame.mixer.Sound('sounds/whicked-sick.ogg'),
				"triple": pygame.mixer.Sound('sounds/3-triple.ogg'),
				"super": pygame.mixer.Sound('sounds/4-super.ogg'),
				# "hyper": pygame.mixer.Sound('sounds/5-hyper.ogg'),
				# "brutal": pygame.mixer.Sound('sounds/6-brutal.ogg'),
				# "master": pygame.mixer.Sound('sounds/7-master.ogg'),
				# "awesome": pygame.mixer.Sound('sounds/8-awesome.ogg'),
				# "blaster": pygame.mixer.Sound('sounds/9-blaster.ogg'),
				# "monster": pygame.mixer.Sound('sounds/10-monster.ogg'),
				# "comboBreaker": pygame.mixer.Sound('sounds/combo-breaker.ogg'),
				# "crowd": pygame.mixer.Sound('sounds/crowd.ogg'),
				# "excellent": pygame.mixer.Sound('sounds/excellent.ogg'),
				# "finishHim": pygame.mixer.Sound('sounds/finish-him.ogg'),
				# "humiliation": pygame.mixer.Sound('sounds/humiliation.ogg'),
				# "superb": pygame.mixer.Sound('sounds/superb.ogg'),
				# "supremeVictory": pygame.mixer.Sound('sounds/supreme-victory.ogg'),
				# "thatWasPathetic": pygame.mixer.Sound('sounds/that-was-pathetic.ogg'),
				# "danger": pygame.mixer.Sound('sounds/danger.ogg'),
				# "wellDone": pygame.mixer.Sound('sounds/well-done.ogg'),
				# "winner": pygame.mixer.Sound('sounds/winner.ogg'),
				# "youllNeverWin": pygame.mixer.Sound('sounds/youll-never-win.ogg'),
				# "victory": pygame.mixer.Sound('sounds/victory.ogg')
			}

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

	def play(self, key):
		print "playing {}".format(key)
		self.channels[key].stop()
		self.channels[key].play(self.audios[key])

	def play1(self):
		self.play("ding")
	def play2(self):
		self.play("triple")
	def play3(self):
		self.play("super")
	def play4(self):
		self.play("wickedSick")

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
