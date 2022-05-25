import pygame
from pygame.sprite import Sprite

class Advocate(Sprite):
	"""A class of the advocate in sideways_shooter"""
	def __init__(self, side_game):
		super().__init__()
		self.screen = side_game.screen
		self.settings = side_game.settings

		# Advocate image and rect attribute.
		self.image = pygame.image.load('images/duque.bmp')
		self.rect = self.image.get_rect()

		# Starting position

		self.rect.x = self.rect.height
		self.rect.y = self.rect.width

		# Store position as an integer
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)

	def check_edges(self):
		self.screen_rect = self.screen.get_rect()
		
		if self.rect.left <= self.screen_rect.left:
			return True

	def update(self):
		"""
		Move the advocate to the left until it hits the sideship, the edge of
		the screen or gets shot down
		"""
		self.x -= self.settings.advocate_speed
		self.rect.x = self.x

class PowerUp(Sprite):
	"""The same as an advocate but helps the ship."""
	def __init__(self, side_game):
		super().__init__()
		self.screen = side_game.screen
		self.settings = side_game.settings

		# Advocate image and rect attribute.
		self.image = pygame.image.load('images/cherry.bmp')
		self.rect = self.image.get_rect()

		# Starting position

		self.rect.x = self.rect.height
		self.rect.y = self.rect.width

		# Store position as an integer
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)

	def check_edges(self):
		self.screen_rect = self.screen.get_rect()
		
		if self.rect.left <= self.screen_rect.left:
			return True

	def update(self):
		"""
		Move the advocate to the left until it hits the sideship, the edge of
		the screen or gets shot down
		"""
		self.x -= self.settings.advocate_speed
		self.rect.x = self.x