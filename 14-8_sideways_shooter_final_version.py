import sys
from time import sleep
import pygame
from pygame import mixer
from sideways_shooter_settings import Settings
from side_game_stats import GameStats
from side_scoreboard import Scoreboard
from side_button import Button
from side_ship import SideShip
from side_ship_bullet import Bullet
from advocate import Advocate
from advocate import PowerUp
from random import randint
from banners import Banner
from banners import StartBanner

class SideShooter:
	"""A ship that shoots bullets to the side."""
	def __init__(self):
		"""Inialize the game and resources."""
		pygame.mixer.pre_init(44100, -16, 2, 64)
		pygame.init()
		pygame.mixer.init()
		self.settings = Settings()
		self.screen = pygame.display.set_mode(
			(self.settings.screen_width, self.settings.screen_height))
		self.screen_rect = self.screen.get_rect()
		pygame.display.set_caption("Side Shooter!!!")

		self.banner = Banner(self)
		self.op_screen = StartBanner(self, 'SideShooter')
		self.stats = GameStats(self)
		self.sb = Scoreboard(self)
		self.side_ship = SideShip(self)
		self.advocate = Advocate(self)

		self.bullets = pygame.sprite.Group()
		self.advocates = pygame.sprite.Group()
		self.power_ups = pygame.sprite.Group()

		# Number of advocates hit since difficulty went up
		self.roll = 0

		# Create the play button
		self.play_button = Button(self, "Play")

	def run_game(self):
		"""Start the main game loop"""
		while True:
			self._check_events()
			mixer.music.pause()
			if self.stats.game_active:
				mixer.music.unpause()
				self._give_power_up()
				self.side_ship.update()
				self._update_bullets()
				self._update_advocates()
				self._update_power_ups()
				self._increase_power()
				self._limit_power()
			self._update_screen()


	def _create_advocate(self):
		"""Creates an advocate at a random point in the right half of the 
		screen.
		"""
		adv = Advocate(self)
		adv_width = adv.rect.width
		available_space = self.screen_rect.right
		random_y = randint(660, 1112)
		adv.x = self.screen_rect.right
		adv.y = available_space - random_y
		adv.rect.x = adv.x
		adv.rect.y = adv.y
		self.advocates.add(adv)

	def _start_music(self):
		"""Start playing some music."""
		chance = randint(1, 5)
		if chance == 1:
			mixer.music.load('music/jojo_background.wav')
		elif chance == 2:
			mixer.music.load("music/background_music_gwyn.wav")
		elif chance == 3:
			mixer.music.load("music/horang suwolga.wav")
		elif chance == 4:
			mixer.music.load("music/let there be light.wav")
		elif chance == 5:
			mixer.music.load("music/soldier_boy.wav")

	def _create_power_up(self):
		"""Shoot a power up from the right side of the screen."""
		# The ship must try to hit the power up.
		p_up = PowerUp(self)
		p_up_width = p_up.rect.width 
		available_space = self.screen_rect.right 
		random_y = randint(660, 1112)
		p_up.x = self.screen_rect.right 
		p_up.y = available_space - random_y
		p_up.rect.x = p_up.x
		p_up.rect.y = p_up.y
		self.power_ups.add(p_up)

	def _increase_power(self):
		"""Increase the power of ship at certain times."""
		if self.settings.long_bullets == True:
			self.settings.bullet_height = self.settings.long_bullet_height

	def _give_power_up(self):
		"""After a roll of 5 randomly decide if a power up is given."""
		collisions = pygame.sprite.spritecollideany(self.side_ship, 
				self.power_ups)
		if collisions:
			self.settings.long_bullets = True
			self.stats.roll = 0

	def _limit_power(self):
		"""After a certain amount of time stop power ups."""
		if self.settings.long_bullets:
			if self.stats.roll == 5:
				self.settings.long_bullets = False
				self.settings.bullet_height = 115

	def _check_play_button(self, mouse_pos):
		"""Start a new game when the player clicks Play."""
		button_clicked = self.play_button.rect.collidepoint(mouse_pos)
		if button_clicked and not self.stats.game_active:
			self._start_music()
			mixer.music.play(-1)
			# Reset the game settings.
			self.settings.initialize_dynamic_settings()
			# Reset the game statstics.
			self.stats.reset_stats()
			self.stats.game_active = True
			self.sb.prep_score()
			self.sb.prep_ships()

			# Get rid of any remainging advocates or bullets
			self.advocates.empty()
			self.bullets.empty()

			# Center the ship
			self.side_ship.center_ship()
			# Hide the mouse cursor
			pygame.mouse.set_visible(False)

	def _check_events(self):
		"""Respond to keyboard and mouse events"""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)
			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)
			elif event.type == pygame.MOUSEBUTTONDOWN:
				mouse_pos = pygame.mouse.get_pos()
				self._check_play_button(mouse_pos)


	def _check_keydown_events(self, event):
		"""Respond to keypresses."""
		if event.key == pygame.K_UP:
			self.side_ship.moving_up = True
		if event.key == pygame.K_DOWN:
			self.side_ship.moving_down = True
		elif event.key == pygame.K_q:
			sys.exit()
		elif event.key == pygame.K_SPACE:
			self._fire_bullet()

	def _check_keyup_events(self, event):
		if event.key == pygame.K_UP:
			self.side_ship.moving_up = False
		elif event.key == pygame.K_DOWN:
			self.side_ship.moving_down = False

	def _fire_bullet(self):
		"""Fire a bullet from the ship"""
		if len(self.bullets) < self.side_ship.settings.bullets_allowed:
			new_bullet = Bullet(self)
			self.bullets.add(new_bullet)
			

	def _update_bullets(self):
		"""Update the positon of bullets and get rid of old bullets"""
		self.bullets.update()

		# Get rid of bullets that have disappeared
		for bullet in self.bullets.copy():
			if bullet.rect.midleft >= self.screen_rect.midright:
				self.bullets.remove(bullet)
		self._check_bullet_advocate_collisions()

	def _check_bullet_advocate_collisions(self):
		"""Check if bullet and advocate have collied and remove them."""
		collisions = pygame.sprite.groupcollide(
				self.bullets, self.advocates, True, True)
		if collisions:
			for advocates in collisions.values():
				self.stats.score += (self.settings.advocate_points
					 * len(advocates))
			self.sb.prep_score()
			self.sb.check_high_score()
			self.stats.roll += 1
			self._check_roll()

			chance = randint(1, 15)
			if chance == 1 and len(self.power_ups) < 1:
				self._create_power_up()


		if not self.advocates:
			self._create_advocate()

	def _check_roll(self):
		"""Check the amount of advoates hit so that difficulty can increase."""
		if self.stats.roll > 5:
			self.settings.increase_speed()
			self.stats.roll = 0

	def _update_power_ups(self):
		"""Update the current power_up"""
		self.power_ups.update()

		# Check to see if any power_up fly off the screen
		self._check_power_ups_left()

	def _update_advocates(self):
		"""Update the current advocates' positions"""
		self.advocates.update()
		# Look for advocate-ship collisions
		if pygame.sprite.spritecollideany(self.side_ship, self.advocates):
			self._ship_hit()

		# Check to see if any advocates fly off the screen
		self._check_advocates_left()

	def _check_advocates_left(self):
		"""Check if an advocate flew off the left edge of the screen."""
		for advocate in self.advocates.copy():
			if advocate.rect.left <= self.screen_rect.left:
				self._ship_hit()

	def _check_power_ups_left(self):
		"""Check if a power up flies off the left edge of the screen."""
		for power_up in self.power_ups.copy():
			if power_up.rect.left <= self.screen_rect.left:
				self.power_ups.remove(power_up)


	def _ship_hit(self):
		"""Respond to the ship being hit by an advocate."""
		if self.stats.ships_left > 0:
			# Decrement ships left
			self.stats.ships_left -= 1
			self.sb.prep_ships()

			# Get rid of any remaining aliens and bullets.
			self.advocates.empty()
			self.bullets.empty()

			# Create another ship.
			self.side_ship.center_ship()

			# Pause.
			sleep(0.5)

		else:
			self.stats.game_active = False
			pygame.mouse.set_visible(True)

	def _update_screen(self):
		"""Update the objects on the screen and flip to the new screen."""
		self.screen.fill(self.settings.bg_color)
		self.side_ship.blitme()

		for bullet in self.bullets.sprites():
			bullet.draw_bullet()
		
		self.power_ups.draw(self.screen)
		self.advocates.draw(self.screen)
		

		# Draw the banner at the top of the screen.
		self.banner.draw_banner()
		# Draw the score information
		self.sb.show_score()

		if not self.stats.game_active:
			self.op_screen.draw_banner()
			self.play_button.draw_button()
		
		pygame.display.flip()


if __name__ == '__main__':
	sg = SideShooter()
	sg.run_game()