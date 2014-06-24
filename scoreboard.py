import pygame, termios, fcntl, sys, os, random
from lib import config, audio_handler, button_handler, game_controller
from espeak import espeak
from threading import Timer

class scoreboard():
	def __init__(self):
		print "constructor"
		self.config = config.config()
		self.ac = audio_handler.audio_handler(self.config)
		self.bc = button_handler.button_handler(self.config)
		self.gc = game_controller.game_controller(self.config)
		self.looping = True
		self.keyboard_handlers = { 'q': self.quit }
		self.combos = {	2: 'dominating',
				3: 'triple',
				4: 'super',
				5: 'hyper',
				6: 'brutal',
				7: 'master',
				8: 'awesome',
				9: 'blaster',
				10: 'monster' }
		self.bc.add_handler('a', self.button_a_onclick)
		self.bc.add_handler('b', self.button_b_onclick)
		self.bc.add_handler('c', self.button_c_onclick)
		self.gc.add_handler('victory', self.on_game_victory)
		self.gc.add_handler('danger_zone', self.on_danger_zone)
		self.gc.add_handler('first_blood', self.on_first_blood)
		self.gc.add_handler('combo_breaker', self.on_combo_breaker)
		self.score_player = None

	def terminate(self):
		self.ac.terminate()
		self.bc.terminate()

	def quit(self):
		print "quiting"
		self.looping = False

	def button_a_onclick(self):
		self.on_score('white')

	def button_b_onclick(self):
		self.on_score('black')

	def button_c_onclick(self):
		print 'start game'
		self.gc.reset()
		self.ac.stop()
		self.ac.play("crowd")
		if self.score_player is not None:
			self.score_player.cancel()
		self.gc.reset()

	def on_score(self, label):
		print 'goal player {}'.format(label)
		self.ac.play("ding")
		self.play_score()
		self.gc.score(label)
		self.play_combo()

	def on_game_victory(self, winner, loser):
		self.ac.play("victory")
		self.ac.play("winner", 2.0)
		self.ac.play("crowd")
		if self.score_player is not None:
			self.score_player.cancel()
		if loser.goal_counter < 5:
			self.play_random_humilliation()
		print "on victory, player {} wins".format(winner.label)

	def on_danger_zone(self, winner, loser):
		self.ac.play("danger")
		self.ac.play("finishHim", delay = 3.5)

	def on_first_blood(self, player, other):
		self.ac.play("firstBlood", 0.5)

	def on_combo_breaker(self, player, other):
		self.ac.play("comboBreaker")

	def play_random_humilliation(self):
		options = {0: 'humiliation', 1:'youllNeverWin', 2:'thatWasPathetic', 3:'supremeVictory'}
		option = random.randrange(0,3)
		print 'humiliation: {}'.format(option)
		self.ac.play(options[option], delay = 5.0)

	def play_score(self):
		if self.score_player is not None:
			self.score_player.cancel()
		self.score_player = Timer(2.5, self.play_score_delayed)
		self.score_player.start()

	def play_score_delayed(self):
		score1 = self.gc.player1.goal_counter
		score2 = self.gc.player2.goal_counter
		if score1 != score2:
			self.synth('{} a {}!'.format(score1, score2))
		else:
			self.synth('empate, a {}!'.format(score1))

	def synth(self, message):
		os.system('espeak -ves+m5 "{}" --stdout -a 500 -s 140 -p 80 | aplay'.format(message))

	def play_combo(self):
		player = self.gc.get_scored_player()
		other = self.gc.get_other_player(player)
		if not player.winner and player.combo_counter in self.combos:
			combo = self.combos[player.combo_counter]
			if player.combo_counter == 3 and other.goal_counter == 0:
				combo = 'wickedSick'
			self.ac.play(combo, 0.6)

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
					if c in self.keyboard_handlers:
						self.keyboard_handlers[c]()
				except IOError: pass
		finally:
			self.terminate()
			termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
			fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)


scoreboard().run()

		
