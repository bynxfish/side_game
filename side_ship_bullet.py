import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	"""A class to mangage bullets fired from the side ship."""
	def __init__(self, side_game):
		super().__init__()
		self.settings = side_game.settings
		self.screen = side_game.screen
		self.color = side_game.settings.bullet_color

		# Create a bullet at 0, 0 and then set correct position
		self.rect = pygame.Rect(0, 0, self.settings.bullet_width, 
				self.settings.bullet_height)
		
		self.rect.midright = side_game.side_ship.rect.midright

		# Store the bullet's positon as a decimal value.
		self.x = float(self.rect.x)

	def update(self):
		"""Move the bullet across the screen horizontally."""
		# Update the decimal position of the bullet.
		self.x += self.settings.bullet_speed

		# Update the rect
		self.rect.x = self.x

	def draw_bullet(self):
		"""Draw the bullet to the screen."""
		pygame.draw.rect(self.screen, self.color, self.rect)
