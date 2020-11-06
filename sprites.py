import settings
import random

class Cactus:
	def __init__(self, speed):
		self.image = random.choice(settings.cactuses_images)
		self.x = settings.SCREENWIDTH + 100 + random.randrange(-80, 60)
		self.y = settings.SCREENHEIGHT - 50 - self.image.get_height()
		self.speed = speed
		self.width = self.image.get_width()

	def move(self, surface):
		if self.x >= -self.width:
			surface.blit(self.image, (self.x, self.y))
			self.x -= self.speed
			return True
			
		else:
			self.x = settings.SCREENWIDTH + 100 + random.randrange(-80, 60)
			return False

	def return_self(self, radius):
		self.x = radius

	def update_image(self):
		self.image = random.choice(settings.cactuses_images)
		self.y = settings.SCREENHEIGHT - 50 - self.image.get_height()

class Dino:
	def __init__(self, dino_x, dino_y):
		self.image = settings.images['dino_stand']
		self.x = dino_x
		self.y = dino_y + 10
		self.make_jump = False
		self.jump_counter = 22
		self.image_counter = 0

	def jump(self):
		if self.jump_counter >= -22:
			self.y -= self.jump_counter / 1.5
			self.jump_counter -= 1
		else:
			self.jump_counter = 22
			self.make_jump = False

	def play_jump_sound(self, sound):
		if self.make_jump and self.jump_counter == 22:
			sound.play()

	def play_animation(self, surface, images_array):
		if self.image_counter == 20:
			self.image_counter = 0

		surface.blit(images_array[self.image_counter // 11], (self.x, self.y))
		self.image_counter += 1
