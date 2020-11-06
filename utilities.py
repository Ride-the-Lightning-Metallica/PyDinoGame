import sys
import os
import pygame
import random


def load_image(name, colorkey = None, directory = 'images'):
	"""Take one required argument and second optional argument.
	Builds a complete platform independent path and load image. 
	If there is colorkey set colorkey. Return pygame surface."""

	fullname = os.path.join(directory, name)
	try:
		image = pygame.image.load(fullname)
	except pygame.error as message:
		print('Cannot load image: ' + name)
		raise SystemExit(message)

	if colorkey is not None:
		if colorkey is -1:
			colorkey = image.get_at((0, 0))
		image.set_colorkey(colorkey)
	return image
	

def load_sound(name, directory = 'audio'):
	pygame.mixer.init()
	class NoneSound:
		def play(self):
			pass

	# Variable with the extension for the sound file depending on the platform
	if 'win' in sys.platform:
		sound_extension = '.wav'
	else:
		sound_extension = '.ogg'

	if not pygame.mixer or not pygame.mixer.get_init():
		return NoneSound
	fullname = os.path.join(directory, name)
	fullname += sound_extension
	try:
		sound = pygame.mixer.Sound(fullname)
	except pygame.error as message:
		print('Cannot load sound: ' + name)
		raise SystemExit(message)
	return sound

def draw_counter(text, size, surface_width):
	pygame.font.init()

	count = text
	font = pygame.font.Font(None, size)
	text = font.render(str(text), 1, (255, 255, 255))
	textpos = text.get_rect(centerx = surface_width - text.get_width() - 20, centery = 20)

	return text, textpos


def play_point_sound(count, sound):
	count = round(count, 1)
	result = str(round(count / 100, 2))[-1]
	if '.0' in str(count) and result == '0':
		sound.play()
		

def create_cactus_array(array, screen_width, class_, surface):
	for index in range(5):
		array.append(class_(5))
	for cactus in array:
		cactus.x = find_radius(array, screen_width)


def find_radius(array, screen_width):
	maximum = max([cactus.x for cactus in array])

	if maximum < screen_width:
		radius = screen_width
		if radius - maximum < 50:
			radius += 150

	else:
		radius = maximum

		choice = random.randrange(0, 5)

		if choice == 0:
			radius += random.randrange(10, 15)
		else:
			radius += random.randrange(200, 350)

	return radius


def draw_array(array, screen_width, surface):
	for cactus in array:
		check = cactus.move(surface)
		if not check:
			radius = find_radius(array, screen_width)
			cactus.update_image()
			cactus.return_self(radius)
