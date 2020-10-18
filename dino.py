import pygame
import random

from settings import *

pygame.init()

screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
pygame.display.set_caption('PyDino Game')
clock = pygame.time.Clock()
background = pygame.Surface(screen.get_size())
screen.blit(background, (0, 0))
show_welcome = True

for index in range(3):
	cactuses_coordinats.append([random.randrange(650, 900), cactus_y])


def dino_jump():
	global dino_y, make_jump, jump_counter
	
	if jump_counter >= -20:
		dino_y -= jump_counter / 1.5
		jump_counter -= 1
	else:
		jump_counter = 20
		make_jump = False


def cactus_move():
	global cactus_x
	cactus_x -= 4

	if cactus_x < 0:
		cactus_x = SCREENWIDTH - 30


def draw_dino_animation():
	global image_counter
	if image_counter == 20:
		image_counter = 0

	background.blit(dino_images[image_counter // 11], (dino_x, dino_y + 10))
	image_counter += 1


while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()
		elif (event.type == pygame.KEYDOWN and event.key == pygame.K_UP and show_welcome):
			show_welcome = False
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:	
			make_jump = True
			if make_jump and jump_counter == 20:
				sounds['jump'].play()
			

	screen.blit(background, (0, 0))
	background.blit(images['background'], (0, -30))
	background.blit(images['ground'], (-70, SCREENHEIGHT - 50))


	if show_welcome:
		background.blit(images['message'], images['message'].get_rect())
		background.blit(images['dino_stand'], (dino_x, SCREENHEIGHT - 50 - images['dino_stand'].get_height()))

	elif not show_welcome:
		draw_dino_animation()
		
		for cactus in cactuses_coordinats:
			cactus[0] -= 4

			if cactus[0] < -30:
				cactus[0] = random.randrange(650, 900)
			
		for cactus in cactuses_coordinats:
			background.blit(images['cactus'], (cactus[0], cactus_y))

		if make_jump:
			dino_jump()

	pygame.display.update()
	clock.tick(FPS)
