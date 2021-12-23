import pygame
import os

WIDTH,HEIGHT=900,500

tank_width,tank_height= 80,60

WHITE=(255,255,255)

Background=pygame.image.load(os.path.join('assets','background.png'))

tank_num_1=pygame.image.load(os.path.join('assets','TankImage.png'))

tank_num_1_resized=pygame.transform.rotate(pygame.transform.scale(tank_num_1,(tank_width,tank_height)),360)

tank_num_2=pygame.image.load(os.path.join('assets','tank_two.png'))

tank_num_2_resized=pygame.transform.rotate(pygame.transform.scale(tank_num_2,(tank_width,tank_height)),360)

WIN=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("tank game")

FPS=60

def draw_window():
	WIN.blit(Background,(0,0))
	
	WIN.blit(tank_num_1_resized,(50,441))

	WIN.blit(tank_num_2_resized,(700,441))

	pygame.display.update()

def main():
	Clock=pygame.time.Clock()


	run=True

	while run:

		Clock.tick(FPS)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run= False

		draw_window()

	pygame.quit()

if __name__== "__main__":
	main()
