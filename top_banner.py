import pygame

class Banner:
	def __init__(self, side_game):
		"""Initialize button attributes."""
		self.screen = side_game.screen
		self.screen_rect = self.screen.get_rect()

		# Set the dimensions of the banner.
		self.width, self.height = 1200, 60
		self.banner_color = 70, 141, 202

		# Build the buttons rect object and map it.
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.midtop = self.screen_rect.midtop
	def draw_banner(self):
		"""Draw blank banner."""
		self.screen.fill(self.banner_color, self.rect)
