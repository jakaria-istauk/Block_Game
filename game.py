# import library here
import pygame

# Pygame module initialised 
pygame.init()

width = 800
height = 600
green = (0, 153, 51)
player_pos = [400, 300]
player_size = 50

screen = pygame.display.set_mode((width, height))

game_over = False

while not game_over:

	for event in pygame.event.get():
		

		if event.type == pygame.QUIT:
			pygame.quit()


	pygame.draw.rect(screen, green, (player_pos[1], player_pos[2], 50, 50))

	pygame.display.update()