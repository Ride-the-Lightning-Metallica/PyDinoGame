import sys
import os
import pygame


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
