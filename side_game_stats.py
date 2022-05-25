import json

class GameStats:
	"""Initialize statistics for side shooter"""
	def __init__(self, side_game):
		"""Initialize statistics."""
		self.settings = side_game.settings
		self.reset_stats()
	
		# Start side shooter in an inactive state
		self.game_active = False

		# High score should never be reset.
		filename = 'side_game_high_score.json'
		with open(filename) as f:
			self.high_score = json.load(f)

	def reset_stats(self):
		"""Initialize statistics that can change during the game."""
		self.ships_left = self.settings.ship_limit
		self.score = 0
		self.roll = 0