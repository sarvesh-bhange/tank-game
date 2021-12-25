import pygame
import os

WIDTH,HEIGHT=900,500

vel=5

tank_width,tank_height= 80,60

WHITE=(255,255,255)




turret_width,turret_height= 110,15

Background=pygame.image.load(os.path.join('assets','background.png'))

tank_num_1=pygame.image.load(os.path.join('assets','tank1.png'))

tank_num_1_resized=pygame.transform.rotate(pygame.transform.scale(tank_num_1,(tank_width,tank_height)),360)

tank_num_2=pygame.image.load(os.path.join('assets','tank2.png'))

tank_num_2_resized=pygame.transform.rotate(pygame.transform.scale(tank_num_2,(tank_width,tank_height)),360)

turret_1=pygame.image.load(os.path.join('assets','tank_turret1.png'))

turret_1_resized=pygame.transform.rotate(pygame.transform.scale(turret_1,(turret_width,turret_height)),360)

turret_2=pygame.image.load(os.path.join('assets','tank_turret2.png'))

turret_2_resized= pygame.transform.scale(turret_2,(turret_width,turret_height))

WIN=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Tank Game")

FPS=60

def tank_1_movement(keys_pressed,tank_1):
	if keys_pressed[pygame.K_a]:
		tank_1.x -= vel

	if keys_pressed[pygame.K_d]:
		tank_1.x += vel

def tank_2_movement(keys_pressed,tank_2):
	if keys_pressed[pygame.K_LEFT]:
		tank_2.x -= vel

	if keys_pressed[pygame.K_RIGHT]:
		tank_2.x += vel

def turret_1_rotate(keys_pressed,turret_1_angle):
	if keys_pressed[pygame.K_w]:
		turret_1_angle += 1

	if keys_pressed[pygame.K_s]:
		turret_1_angle -= 1

	return turret_1_angle


def draw_window(tank_1,tank_2,turret_1_angle):
	WIN.blit(Background,(0,0))
	
	WIN.blit(tank_num_1_resized,(tank_1))

	WIN.blit(tank_num_2_resized,(tank_2))

	turret_1_rotated = pygame.transform.rotate(turret_1_resized,turret_1_angle)

	WIN.blit(turret_1_rotated,(tank_1.x+37,tank_1.y+3))

	WIN.blit(turret_2_resized,(tank_2.x-68,tank_2.y+3))

	pygame.display.update()

def main():
	tank_1=pygame.Rect(10,445,tank_width,tank_height)

	tank_2=pygame.Rect(800,443,tank_width,tank_height)

	turret_1_angle = 360

	turret_2_angle= 360

	turret_1=pygame.Rect(10,455,turret_width,tank_height)

	turret_2=pygame.Rect(800,443,turret_width,tank_height)

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

		turret_1_angle =  turret_1_rotate(keys_pressed, turret_1_angle)

		draw_window(tank_1,tank_2,turret_1_angle)

	pygame.quit()

if __name__== "__main__":
	main()
