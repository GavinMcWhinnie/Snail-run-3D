import pygame
import numpy as np

### own modules
import cube, translate

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
    return (int(point[0]), int(point[1]))

def draw_cube(cube):
    for face, color in cube.return_faces(screen_position, darkness):
        points = [get_point(point) for point in face]
        pygame.draw.polygon(screen, color, points, 0)
    #print(get_point(cube.return_faces(screen_position)[1]))
    for side in cube.return_sides(screen_position):
        start = get_point(side[0])
        end = get_point(side[1])
        pygame.draw.line(screen, BLACK, start, end, 1)
    #pygame.draw.circle(screen, RED, (get_point(cube.return_faces(screen_position, darkness)[1])), 5, 0)

pygame.init()

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Snail Run 3D")
clock = pygame.time.Clock()

### create stuff:
cube1 = cube.Cuboid(200, 400, 350, [0, 0, 0], ORANGE)

### set screen/camera position for translate
screen_position = np.array([1000,1000,1000])
screen_direction = np.array([-1,-1,-1])
viewer_distance = 1000
darkness = 0

running = True

_up = False
_down = False

while running:

    clock.tick(30)

    ### handle pygame events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                _up = True
            if event.key == pygame.K_DOWN:
                _down = True
            if event.key == pygame.K_0:
                running = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                _up = False
            if event.key == pygame.K_DOWN:
                _down = False
        if event.type == pygame.QUIT:
            running = False

    ### clear the screen and start drawing
    screen.fill((WHITE))

    draw_cube(cube1)
    cube1.rotate([1,1,1])
    if _up:
        pass
    elif _down:
        pass

    ### update the screen
    pygame.display.flip()

pygame.quit()
