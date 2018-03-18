############ Snail Run 3D ################
######## Made by Gavin McWhinnie #########

import pygame
import numpy as np

### own modules
import characters, translate

### colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
ORANGE = (255, 153, 0)
BROWN = (153, 51, 0)
AQUA = (0, 255, 255)
SKY_BLUE = (230, 255, 255)

### game display size
WIDTH = 500
HEIGHT = 500

def get_point(point):
    point = translate.translate(point, screen_position, screen_direction, viewer_distance)
    point[0] += WIDTH/2
    point[1] = -point[1] + HEIGHT/2
    return (point[0], point[1])

def draw_character(character, with_lines):
    for cube, color in character.return_faces(screen_position):
        for face in cube:
            points = [get_point(point) for point in face]
            pygame.draw.polygon(screen, color, points, 0)
    if with_lines:
        for cube, color in character.return_sides():
            for side in cube:
                start = get_point(side[0])
                end =  get_point(side[1])
                pygame.draw.line(screen, BLACK, start, end, 1)

"""
def draw_character(character):
    for cube in character.return_cubes():
        #iterates through the cubes in a character, sorted with the closest to
        #the camera first.
        for face, color in cube.return_faces():
            #draw that face
            pass
        for side, color in cube.return_sides():
            #draw that edge
            pass
"""

pygame.init()

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Snail Run 3D")
clock = pygame.time.Clock()

### create stuff:

logo = pygame.image.load('logo.png')
bob = characters.Snail([0,0,-400])
big_font = pygame.font.SysFont('Calibri', 25, True, False)
small_font = pygame.font.SysFont('Calibri', 15, True, False)
start_message = big_font.render("Press Space to Play", True, BLACK)
glitch_message = small_font.render("(Warning: it's glitchy)", True, BLACK)


### set screen/camera position for translate

screen_position = np.array([1000,1000,1000])
screen_direction = np.array([-1,-1,-1])
viewer_distance = 1000

### main game loop
running = True
game_stage = "Title"

show_lines = True
while running:

    clock.tick(10)

    ### handle pygame events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                pass
            if event.key == pygame.K_DOWN:
                pass
            if event.key == pygame.K_SPACE:
                game_stage = "Begin"
            if event.key == pygame.K_0:
                if show_lines:
                    show_lines = False
                else:
                    show_lines = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                pass
            if event.key == pygame.K_DOWN:
                pass
        if event.type == pygame.QUIT:
            running = False

    ### clear the screen and start drawing
    screen.fill((WHITE))

    if game_stage == "Title":
        screen.blit(logo, (90,70))
        screen.blit(start_message, (150, 450))
        screen.blit(glitch_message, (300, 250))
        bob.rotate([0,0,5])
        draw_character(bob, show_lines)
        


    ### update the screen
    pygame.display.flip()

pygame.quit()
