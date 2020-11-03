from utilities import load_image, load_sound

# Settings for window
FPS = 60
SCREENWIDTH = 600
SCREENHEIGHT = 300


# Images and sounds dicts
images, sounds = {}, {}

# Add images for background, message(welcome message), game over(if player lose) and ground
images['background'] = load_image('background.jpg')
images['message'] = load_image('message.png', colorkey = (255, 255, 255))
images['gameover'] = load_image('gameover.png')
images['ground'] = load_image('ground.jpg')

# Add images of dino in different positions 
images['dino_stand'] = load_image('dino_stand.png')
images['dino_right'] = load_image('dino_right.png')
images['dino_left'] = load_image('dino_left.png')

# Add image of cactus
images['cactus'] = load_image('cactus.png')


# Dino settings
dino_x = 10
dino_y = SCREENHEIGHT - 60 - images['dino_right'].get_height()
make_jump = False
jump_counter = 22
dino_right = True
dino_images = [images['dino_right'], images['dino_left']]
image_counter = 0


# Cactus settings
cactus_x = SCREENWIDTH - 30
cactus_y = SCREENHEIGHT - 50 - images['cactus'].get_height()
cactuses = []
cactuses_x = [cactus_x + SCREENWIDTH for additional_x in [30, 200, 430,
																		 590, 750]]


# Add sounds for collide with cactus, jump, point and defeat
sounds['hit'] = load_sound('hit')
sounds['jump'] = load_sound('wing')
sounds['point'] = load_sound('point')
sounds['defeat'] = load_sound('die')

# Counter
count = 0
discharge_counter = 0
