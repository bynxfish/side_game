class Settings:
	"""Base settings for SideShooter."""
	def __init__(self):
		"""Initialize the game's settings."""
		self.screen_width = 1200
		self.screen_height = 600
		self.bg_color = (144, 238, 144)

		# Sideship settings
		self.side_ship_speed = 0.5
		self.ship_limit = 5

		# Bullet settings
		self.long_bullet_height = 300
		self.bullets_allowed = 5
		self.bullet_color= (255, 255, 167)
		self.bullet_height = 115
		self.bullet_width = 5

		# How quickly the game speeds up
		self.speedup_scale = 1.05

		# How quickly the advocate point values increase
		self.score_scale = 1.5

		# Power ups
		self.long_bullets = False
		self.firewall = False


		self.initialize_dynamic_settings()

	def initialize_dynamic_settings(self):
		"""Initialize settings that change throughout the game."""
		self.side_ship_speed = 0.5
		self.bullet_speed = 1
		self.advocate_speed = 1

		# Scoring
		self.advocate_points = 50

	def increase_speed(self):
		"""Initialize speed settings and alien point values."""
		self.side_ship_speed *= self.speedup_scale
		self.bullet_speed *= self.speedup_scale
		self.advocate_speed *= self.speedup_scale

		self.advocate_points = int(self.advocate_points * self.score_scale)

