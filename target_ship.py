import pygame

class Ship:
	"""A Ship the will move up and down and fire bullets."""
	
	def __init__(self, tg):
		"""Define starting attributes for the ship."""
		self.settings = tg.settings
		self.screen = tg.screen
		self.screen_rect = tg.screen.get_rect()
		self.ship_speed = 2

		# Load the image and set it's rect
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()

		# Start each new ship in the middle left of the screen.
		self.rect.midleft = self.screen_rect.midleft

		# Store a decimal value for the ship's vertical position.
		self.y = float(self.rect.y)

		# Movement flags.
		self.moving_up = False
		self.moving_down = False

	def update(self):
		"""Update the ship's position based on the movement flag."""
		# Update the ship's y value not the rect.
		if self.moving_up and self.rect.top >= 0:
			self.y -= self.settings.ship_speed
		if self.moving_down and self.rect.bottom <= self.screen_rect.bottom:
			self.y += self.settings.ship_speed

		# Update rect object
		self.rect.y = self.y 

	def blitme(self):
		"""Draw the ship at it's current location."""
		self.screen.blit(self.image, self.rect)

	def center_ship(self):
		"""Center the ship in the middle of the left edge of the screen."""
		self.rect.midleft = self.screen_rect.midleft
		self.y = float(self.rect.y)
