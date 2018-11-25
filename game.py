# import library here
import pygame
import sys
import random

# Pygame module initialised 
pygame.init()

width = 800
height = 600

green = (0, 153, 51)
red = (255, 0, 0)
bg_color = (179, 153, 255)
yellow = (255,255,0)

player_size = 50
player_pos = [width/2, height-2*player_size]

enemy_size = 50
enemy_pos = [random.randint(0, width-enemy_size), 0]
enemy_list = [enemy_pos]

speed = 10

screen = pygame.display.set_mode((width, height))

game_over = False

score = 0

clock = pygame.time.Clock()

myFont = pygame.font.SysFont("comicsansms", 35)

def set_level(score, speed):
	if score < 20:
		speed = 6
	elif score < 40:
		speed = 8
	elif score <60:
		speed = 10
	else:
		speed = 15

	# speed = score/5 + 1
	return speed

def drop_enemies(enemy_list):
	delay = random.random()
	if len(enemy_list) < 10 and delay < 0.2:
		x_pos = random.randint(0,width-enemy_size)
		y_pos = 0
		enemy_list.append([x_pos, y_pos])

def drow_enemies(enemy_list):
	for enemy_pos in enemy_list:
		pygame.draw.rect(screen, red, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))

def update_enemy_position(enemy_list, score):
	for idx, enemy_pos in enumerate(enemy_list):
		if enemy_pos[1] >= 0 and enemy_pos[1] < height:
			enemy_pos[1] += speed
		else:
			enemy_list.pop(idx)
			score += 1
	return score

def collision_check(enemy_list, player_pos):
	for enemy_pos in enemy_list:
		if detect_collision(enemy_pos, player_pos):
			return True
	return False

def detect_collision(player_pos, enemy_pos):
	p_x = player_pos[0]
	p_y = player_pos[1]

	e_x = enemy_pos[0]
	e_y = enemy_pos[1]

	if (e_x >= p_x and e_x < (p_x + player_size)) or (p_x >= e_x and p_x < (e_x + enemy_size)):
		if(e_y >= p_y and e_y < (p_y + player_size)) or (p_y >= e_y and p_y < (e_y + enemy_size)):
			return True
	return False

while not game_over:

	for event in pygame.event.get():
		

		if event.type == pygame.QUIT:
			sys.exit()

		if event.type == pygame.KEYDOWN:

			x = player_pos[0]
			y = player_pos[1]

			if event.key == pygame.K_LEFT:
				x -= player_size/2

			elif event.key == pygame.K_RIGHT:
				x += player_size/2

			player_pos = [x,y]

	screen.fill(bg_color)

	#Updating enemy position
	# if enemy_pos[1] >= 0 and enemy_pos[1] < height:
	# 	enemy_pos[1] += speed
	# else:
	# 	enemy_pos[0] = random.randint(0, width-enemy_size)
	# 	enemy_pos[1] = 1

	drop_enemies(enemy_list)
	score = update_enemy_position(enemy_list, score)
	speed = set_level(score, speed)

	drow_enemies(enemy_list)

	text = "Score: "+ str(score)
	label = myFont.render(text, 1, yellow)
	screen.blit(label, (width-200, height-60))

	if collision_check(enemy_list, player_pos):
		game_over = True
		break 
	
	pygame.draw.rect(screen, green, (player_pos[0], player_pos[1], player_size, player_size))

	clock.tick(10)

	pygame.display.update()


print("Your Score is: " + str(score))

screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
done = False

font = pygame.font.SysFont("comicsansms", 72)
text = font.render("Your Score is: "+ str(score) , True, (0, 128, 0))

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True
    
    screen.fill((255, 255, 255))
    screen.blit(text, (320 - text.get_width() // 2, 240 - text.get_height() // 2))
    
    pygame.display.flip()
    clock.tick(0)
