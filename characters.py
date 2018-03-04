import numpy as np
import cube

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
ORANGE = (255, 153, 0)
BROWN = (153, 51, 0)
AQUA = (0, 255, 255)
LIGHT_GREY = (242, 242, 242)

class Snail():

    def __init__(self, origin, rotation=None):

        self.origin = np.array(origin)
        if rotation == None:
            rotation = [0, 0, 0]
        self.rotation = np.array(rotation)
        self.create_cubes()

    def create_cubes(self):
        self.cubes = []

        head_position = cube.rotate_vector(np.array([0,-100,0]), self.rotation)
        head = cube.Cube(40, self.origin + head_position, GREEN, self.rotation)
        self.cubes.append(head)
        
        eye_holder_1_position = cube.rotate_vector(np.array([32, -132, 60]), self.rotation)
        eye_holder_1 = cube.Cuboid(16, 16, 40, self.origin + eye_holder_1_position, GREEN, self.rotation)
        self.cubes.append(eye_holder_1)
        
        eye_holder_2_position = cube.rotate_vector(np.array([-32, -132, 60]), self.rotation)
        eye_holder_2 = cube.Cuboid(16, 16, 40, self.origin + eye_holder_2_position, GREEN, self.rotation)
        self.cubes.append(eye_holder_2)
        
        eye_1_position = cube.rotate_vector(np.array([32, -132, 100]), self.rotation)
        eye_1 = cube.Cube(20, self.origin + eye_1_position, LIGHT_GREY, self.rotation)
        self.cubes.append(eye_1)

        eye_2_position = cube.rotate_vector(np.array([-32, -132, 100]), self.rotation)
        eye_2 = cube.Cube(20, self.origin + eye_2_position, LIGHT_GREY, self.rotation)
        self.cubes.append(eye_2)

        shell_position = cube.rotate_vector(np.array([0, 40, 60]), self.rotation)
        shell = cube.Cuboid(120, 200, 200, self.origin + shell_position, ORANGE, self.rotation)
        self.cubes.append(shell)

    def return_sides(self):
        cubes_sides = []
        for cube in self.cubes:
            cubes_sides.append(cube.return_sides())
            
        return cubes_sides

    def return_faces(self, screen_position):
        cubes_faces = []
        cubes_magnitudes = {}
        for current_cube in self.cubes:
            cube_to_screen = screen_position - current_cube.origin
            magnitude = np.sqrt(cube_to_screen.dot(cube_to_screen))
            cubes_magnitudes[magnitude] = current_cube
        for key in reversed(sorted(cubes_magnitudes)):
            cubes_faces.append(cubes_magnitudes[key].return_faces(screen_position))

        return cubes_faces

    def update(self):
        self.create_cubes()

    def rotate(self, rotation):
        self.rotation[0] = (self.rotation[0] + rotation[0]) % 360
        self.rotation[1] = (self.rotation[1] + rotation[1]) % 360
        self.rotation[2] = (self.rotation[2] + rotation[2]) % 360
        self.update()
        


        
