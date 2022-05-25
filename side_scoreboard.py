import pygame.font
from pygame.sprite import Group
from side_ship import SideShip
import json

class Scoreboard:
	"""A class to report coring informationn."""

	def __init__(self, side_game):
		"""Initialize scorekeeping attributes."""
		self.side_game = side_game
		self.screen = side_game.screen
		self.screen_rect = self.screen.get_rect()
		self.settings = side_game.settings
		self.stats = side_game.stats

		# Font settings for scoring information.
		self.text_color = self.side_game.settings.bg_color
		self.font = pygame.font.SysFont(None, 48)

		# Prepare the initial score images.
		self.prep_score()
		self.prep_high_score()
		self.prep_ships()

	def prep_score(self):
		"""Turn the score into a rendered image."""
		rounded_score = round(self.stats.score, -1)
		score_str = "{:,}".format(rounded_score)
		self.score_image = self.font.render(score_str, True,
				self.text_color, self.side_game.banner.banner_color)

		# Display the score at the top right of the screen.
		self.score_rect = self.score_image.get_rect()
		self.score_rect.right = self.screen_rect.right - 20
		self.score_rect.top = 20

	def show_score(self):
		"""Draw scores, and ships to the screen."""
		self.screen.blit(self.score_image, self.score_rect)
		self.screen.blit(self.high_score_image, self.high_score_rect)
		self.ships.draw(self.screen)

	def prep_high_score(self):
		"""Turn the high score into a rendered image."""
		high_score = round(self.stats.high_score, -1)
		high_score_str = "{:,}".format(high_score)
		self.high_score_image = self.font.render(high_score_str, True,
				self.text_color, self.side_game.banner.banner_color)

		# Center the high score at the top of the screen.
		self.high_score_rect = self.high_score_image.get_rect()
		self.high_score_rect.centerx = self.screen_rect.centerx
		self.high_score_rect.top = self.score_rect.top

	def check_high_score(self):
		"""Check to see if there's a new high score."""
		if self.stats.score >= self.stats.high_score:
			file_name = 'side_game_high_score.json'
			with open(file_name, 'w') as f:
				json.dump(self.stats.score, f)
			self.stats.high_score = self.stats.score
			self.prep_high_score()

	def prep_ships(self):
		"""Show how many ships are left."""
		self.ships = Group()
		for ship_number in range(self.stats.ships_left):
			ship = SideShip(self.side_game)
			ship.image = pygame.image.load('images/side_ship_ships.bmp')
			ship.rect = ship.image.get_rect()
			ship.rect.x = 10 +ship_number * ship.rect.width
			ship.rect.y = -10
			self.ships.add(ship)