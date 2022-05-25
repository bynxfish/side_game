import pygame
from pygame.sprite import Sprite

class SideShip(Sprite):
	"""A ship that shoots to it's side."""
	def __init__(self, side_game):
		"""Initialize ship Attributes."""
		super().__init__()
		self.screen = side_game.screen
		self.screen_rect = side_game.screen.get_rect()
		self.settings = side_game.settings
		self.side_ship_speed = 2.0


		# Load the ship
		self.image = pygame.image.load('images/side_ship.bmp')
		self.rect = self.image.get_rect()

		# Start the ship in the mid left of screen
		self.rect.midleft = self.screen_rect.midleft

		# ship position in decimal value
		self.y = float(self.rect.y)

		# Movemente flags
		self.moving_up = False
		self.moving_down = False

	def update(self):
		"""Update the ship's position based on movement flags."""
		# Update the ship's y value not the rect.
		if self.moving_up and self.rect.top > 60:
			self.y -= self.side_ship_speed
		if self.moving_down and self.rect.bottom <= self.screen_rect.bottom:
			self.y += self.side_ship_speed

		# Update rect object from self.y
		self.rect.y = self.y

	def blitme(self):
		"""draw the side ship at it's current location"""
		self.screen.blit(self.image, self.rect)

	def center_ship(self):
		self.rect.midleft = self.screen_rect.midleft
		self.y = float(self.rect.y)