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
		self.ship_speed = 0.5