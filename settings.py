from utilities import load_image, load_sound, random

# Settings for window
FPS = 60
SCREENWIDTH = 600
SCREENHEIGHT = 300


# Images and sounds dicts
images, sounds = {}, {}

# Add images for background, message(welcome message), game over(if player lose) and ground
images['background'] = load_image('background.jpg')
images['message'] = load_image('message.png', colorkey = (255, 255, 255))
images['game_over'] = load_image('gameover.png')
images['ground'] = load_image('ground.jpg')

# Add images of dino in different positions 
images['dino_stand'] = load_image('dino_stand.png')
images['dino_right'] = load_image('dino_right.png')
images['dino_left'] = load_image('dino_left.png')

# Add images of cactus
images['cactus_middle'] = load_image('cactus_middle.png')
images['cactus_high'] = load_image('cactus_high.png')
images['cactus_low'] = load_image('cactus_low.png')
cactuses_images = [images['cactus_middle'], images['cactus_high'], images['cactus_low']]


# Dino settings
dino_x = 10
dino_y = SCREENHEIGHT - 60 - images['dino_right'].get_height()
dino_images = [images['dino_right'], images['dino_left']]


# Cactus settings
cactuses = []


# Add sounds for collide with cactus, jump, point and defeat
sounds['hit'] = load_sound('hit')
sounds['jump'] = load_sound('wing')
sounds['point'] = load_sound('point')
sounds['defeat'] = load_sound('die')

# Score
count = 0
record = 0