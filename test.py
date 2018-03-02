import pygame, characters, translate
import numpy as np

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

size = (400, 500)
screen = pygame.display.set_mode(size)
screen.fill(WHITE)
pygame.display.set_caption("Snail Run 3D")

woah = 100

bob = characters.Snail([0,0,0])
def draw_bob(woah):
    for cube in bob.return_sides():
        for side in cube:

            screen_position = np.array([100,100,-50])
            screen_direction = np.array([-1,-1,-0.5])
            viewer_distance = 1000
            
            start = translate.translate(side[0], screen_position, screen_direction, viewer_distance)
            end = translate.translate(side[1], screen_position, screen_direction, viewer_distance)
            pygame.draw.line(screen, BLACK, (start[0]+200,start[1]+250), (end[0]+200, end[1]+250), 1)
    pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                woah += 10
            if event.key == pygame.K_DOWN:
                woah -= 10
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)
    draw_bob(woah)

pygame.quit()
