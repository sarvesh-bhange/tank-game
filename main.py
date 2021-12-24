import pygame
import os

WIDTH,HEIGHT=900,500

vel=5

tank_width,tank_height= 80,60

WHITE=(255,255,255)

Background=pygame.image.load(os.path.join('assets','background.png'))

tank_num_1=pygame.image.load(os.path.join('assets','TankImage.png'))

tank_num_1_resized=pygame.transform.rotate(pygame.transform.scale(tank_num_1,(tank_width,tank_height)),360)

tank_num_2=pygame.image.load(os.path.join('assets','tank_two.png'))

tank_num_2_resized=pygame.transform.rotate(pygame.transform.scale(tank_num_2,(tank_width,tank_height)),360)

WIN=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("tank game")

FPS=30

def tank_1_movement(keys_pressed,tank_1):
	if keys_pressed[pygame.K_a] and tank_1.x - vel > 0:
		tank_1.x -= vel

	if keys_pressed[pygame.K_d] and tank_1.x+tank_width + vel < WIDTH:
		tank_1.x += vel

def tank_2_movement(keys_pressed,tank_2):
	if keys_pressed[pygame.K_LEFT] and tank_2.x - vel > 0:
		tank_2.x -= vel

	if keys_pressed[pygame.K_RIGHT] and tank_2.x+tank_width + vel < WIDTH:
		tank_2.x += vel


def draw_window(tank_1,tank_2):
	WIN.blit(Background,(0,0))
	
	WIN.blit(tank_num_1_resized,(tank_1))

	WIN.blit(tank_num_2_resized,(tank_2))

	pygame.display.update()

def main():
	tank_1=pygame.Rect(10,445,tank_width,tank_height)

	tank_2=pygame.Rect(800,443,tank_width,tank_height)

	Clock=pygame.time.Clock()


	run=True

	while run:

		Clock.tick(FPS)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run= False


		keys_pressed= pygame.key.get_pressed()

		tank_1_movement(keys_pressed,tank_1)

		tank_2_movement(keys_pressed,tank_2)

		draw_window(tank_1,tank_2)

	pygame.quit()

if __name__== "__main__":
	main()
