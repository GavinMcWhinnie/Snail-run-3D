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

bob = characters.Snail([0,0,0])
def draw_bob(woah):
    for cube,color in bob.return_sides():
        for side in cube:

            screen_position = np.array([1000,1000,woah + 0.01])
            screen_direction = np.array([-1,-1,-woah/1000 + 0.01])
            viewer_distance = 1000
            
            start = translate.translate(side[0], screen_position, screen_direction, viewer_distance)
            end = translate.translate(side[1], screen_position, screen_direction, viewer_distance)
            pygame.draw.line(screen, BLACK, (start[0]+200,-start[1]+250), (end[0]+200, -end[1]+250), 1)

def draw_bob_magic(woah):

    screen_position = np.array([1000,1000,woah + 0.01])
    screen_direction = np.array([-1,-1,-woah/1000 + 0.01])
    viewer_distance = 1000
    
    for cube, color in bob.return_faces(screen_position):
        for face in cube:

            points = []

            for point in face:
                point = translate.translate(point, screen_position, screen_direction, viewer_distance)
                point[0] += 200
                point[1] = -point[1] + 250
                points.append(point)
            
            pygame.draw.polygon(screen, color, points, 0)

def draw_axis(height):
    screen_position = np.array([1000,1000,height +0.01])
    screen_direction = np.array([-1,-1,-height/1000 + 0.01])
    viewer_distance = 1000
    
    origin = translate.translate(np.array([0,0,0]), screen_position, screen_direction, viewer_distance)

    x_axis = translate.translate(np.array([500,0,0]), screen_position, screen_direction, viewer_distance)
    y_axis = translate.translate(np.array([0,500,0]), screen_position, screen_direction, viewer_distance)
    z_axis = translate.translate(np.array([0,0,500]), screen_position, screen_direction, viewer_distance)

    #print("x, y, z", x_axis, y_axis, z_axis)

    pygame.draw.line(screen, BLACK, (origin[0]+200,-origin[1]+250), (x_axis[0]+200, -x_axis[1]+250), 1)
    pygame.draw.line(screen, BLUE, (origin[0]+200,-origin[1]+250), (y_axis[0]+200, -y_axis[1]+250), 1)
    pygame.draw.line(screen, GREEN, (origin[0]+200,-origin[1]+250), (z_axis[0]+200, -z_axis[1]+250), 1)

height = 1000
moving_up = False
moving_down = False

clock = pygame.time.Clock()

running = True
while running:

    clock.tick(50)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                moving_up = True
            if event.key == pygame.K_DOWN:
                moving_down = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                moving_up = False
            if event.key == pygame.K_DOWN:
                moving_down = False
        if event.type == pygame.QUIT:
            running = False

    screen.fill((230,255,255))
    if moving_up:
        height += 50
    elif moving_down:
        height -= 50
    
    draw_axis(height)
    draw_bob_magic(height)
    draw_bob(height)
    pygame.display.flip()

pygame.quit()
