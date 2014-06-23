import sys

class game_controller(object):

	def __init__(self):
		self.player1 = player('white')
		self.player2 = player('black')
		self.last_scored_player = None

	def reset(self):
		self.player1.reset()
		self.player2.reset()

	def score(self, player_label):
		player = self.player1 if player_label == 'white' else self.player2
		other_player = self.player2 if player == self.player1 else self.player1
		if player is not self.last_scored_player:
			player.combo_breaker()
			other_player.combo_breaker()
		self.last_scored_player = player
		player.score()
		self.player1.show_score()
		self.player2.show_score()


class player(object):
	 
	def __init__(self, label):
		self.label = label
	 	self.goal_counter = 0
		self.combo_counter = 0

	def reset(self):
		print "{}: reset".format(self.label)
		self.goal_counter = 0
		self.combo_counter = 0

	def score(self):
		self.goal_counter += 1
		self.combo_counter += 1

	def show_score(self):
		print "{}: score - {}: combos {}".format(self.label, self.goal_counter, self.combo_counter)

	def combo_breaker(self):
		self.combo_counter = 0


