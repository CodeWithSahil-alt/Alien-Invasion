# Contains a class called Settings to store all these values in one place.

class Settings:
	"""A class to store all settings for Alien Invasion."""

	def __init__(self):
		"""Initialize the game's settings."""
		# Screen settings
		self.screen_width = 1200
		self.screen_height = 755
		self.bg_color = (230, 230, 230)

		# Ship settings
		self.ship_speed = 0.65

		# Bullet settings
		self.bullet_speed = 0.5
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (18, 42, 89)
		self.bullets_allowed = 3

		# Alien settings
		self.alien_speed = 0.3
		self.fleet_drop_speed = 10
		# fleet_direction of 1 represents right; -1 represents left.
		self.fleet_direction = 1