import pygame.font

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

class StartBanner(Banner):
	def __init__(self, side_game, msg):
		"""Initialize button attributes."""
		super().__init__(side_game)
		# Set the dimensions of the banner.
		self.width, self.height = 1200, 600
		self.banner_color = 153, 223, 242
		self.text_color = (204, 242, 149)
		self.font = pygame.font.SysFont('impact', 100)
		# Set the position
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.center = self.screen_rect.center

		self._prep_msg(msg)

	def _prep_msg(self, msg):
		"""Turn msg into a rendered image and map it to the starting screen."""
		self.msg_image = self.font.render(msg, True, self.text_color,
				self.banner_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.centerx = self.screen_rect.centerx + 20

	def draw_banner(self):
		"""Draw opening screen with message."""
		self.screen.fill(self.banner_color, self.rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)