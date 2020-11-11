import pygame

from settings import *
from utilities import *
from sprites import Cactus, Dino

pygame.init()

screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
pygame.display.set_caption('PyDino Game')
clock = pygame.time.Clock()
background = pygame.Surface(screen.get_size())
screen.blit(background, (0, 0))
show_welcome = True
dino = None		

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()
		elif (event.type == pygame.KEYDOWN and event.key == pygame.K_UP and show_welcome):
			show_welcome = False
		elif ((event.type == pygame.KEYDOWN and event.key == pygame.K_UP and show_game_over) or
			dino is None):
			show_game_over = False
			dino = Dino(dino_x, dino_y)
		
			create_cactus_array(cactuses, SCREENWIDTH, Cactus, surface = background)

			all_sprites = pygame.sprite.RenderPlain(cactuses, dino)
			cactuses_sprites = pygame.sprite.RenderPlain(cactuses)
			count = 0
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:	
			dino.make_jump = True
			dino.play_jump_sound(sounds['jump'])
			

	screen.blit(background, (0, 0))
	background.blit(images['background'], (0, -30))
	background.blit(images['ground'], (-70, SCREENHEIGHT - 50))

	if show_game_over:
		record = calculation_record(round(count), record)
		draw_array(cactuses, SCREENWIDTH, background, True)
		game_over(images['game_over'], background, round(count), font_size = 36, record = record)
		background.blit(images['dino_stand'], (dino_x, dino_y + 10))

	if show_welcome:
		background.blit(images['message'], images['message'].get_rect())
		background.blit(images['dino_stand'], (dino_x, dino_y + 10))

	elif not show_welcome and not show_game_over:
		dino.play_animation(background, dino_images)		
		background.blit(*draw_counter(round(count), 23, SCREENWIDTH))

		play_point_sound(count, sounds['point'])

		count += 0.2

		draw_array(cactuses, SCREENWIDTH, background, False)

		all_sprites.update()
		hits = pygame.sprite.spritecollide(dino, cactuses, False)

		if hits:
			show_game_over = True
			hits = []
			cactuses = []

		if dino.make_jump:
			dino.jump()

	pygame.display.update()
	clock.tick(FPS)
