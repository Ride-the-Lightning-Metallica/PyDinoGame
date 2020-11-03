import pygame
import random

from settings import *
from utilities import *

pygame.init()

screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
pygame.display.set_caption('PyDino Game')
clock = pygame.time.Clock()
background = pygame.Surface(screen.get_size())
screen.blit(background, (0, 0))
show_welcome = True

class Cactus:
	def __init__(self, cactus_y, cactus_x, speed):
		self.image = images['cactus']
		self.x = cactus_x
		self.y = cactus_y
		self.speed = speed
		self.width = self.image.get_width()

	def move(self):
		if self.x >= -self.width:
			background.blit(self.image, (self.x, self.y))
			self.x -= self.speed
			return True
			
		else:
			self.x = SCREENWIDTH + 100 + random.randrange(-80, 60)
			return False

	def return_self(self, radius):
		self.x = radius

def dino_jump():
	global dino_y, make_jump, jump_counter
	
	if jump_counter >= -22:
		dino_y -= jump_counter / 1.5
		jump_counter -= 1
	else:
		jump_counter = 22
		make_jump = False


def draw_dino_animation():
	global image_counter
	if image_counter == 20:
		image_counter = 0

	background.blit(dino_images[image_counter // 11], (dino_x, dino_y + 10))
	image_counter += 1
		
create_cactus_array(cactuses, cactuses_x, cactus_y, Cactus)


while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()
		elif (event.type == pygame.KEYDOWN and event.key == pygame.K_UP and show_welcome):
			show_welcome = False
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:	
			make_jump = True
			if make_jump and jump_counter == 22:
				sounds['jump'].play()
			

	screen.blit(background, (0, 0))
	background.blit(images['background'], (0, -30))
	background.blit(images['ground'], (-70, SCREENHEIGHT - 50))


	if show_welcome:
		background.blit(images['message'], images['message'].get_rect())
		background.blit(images['dino_stand'], (dino_x, SCREENHEIGHT - 50 - images['dino_stand'].get_height()))

	elif not show_welcome:
		draw_dino_animation()		
		background.blit(*draw_counter(round(count), 23, SCREENWIDTH))

		play_point_sound(count, sounds['point'])

		count += 0.2

		draw_array(cactuses, SCREENWIDTH)

		if make_jump:
			dino_jump()

	pygame.display.update()
	clock.tick(FPS)
