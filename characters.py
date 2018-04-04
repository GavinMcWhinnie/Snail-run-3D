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
LIGHT_GREY = (128, 127, 127)

class Snail():

    def __init__(self, origin, rotation=None):

        self.origin = np.array(origin)
        if rotation == None:
            rotation = [0, 0, 0]
        self.rotation = np.array(rotation)
        self.connections = {0:[1,2,5],1:[0,3], 2:[0,4], 3:[1], 4:[2], 5:[0]}
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

    def return_cubes(self, screen_position):
        furthest_cubes = []
        furthest_distance = 0
        for cube in range(len(self.cubes)):
            furthest_point, closest_point = self.cubes[cube].return_landmark_points(screen_position)
            point_to_screen = screen_position - self.cubes[cube].points[furthest_point]
            distance = np.sqrt(point_to_screen.dot(point_to_screen))
            if distance == furthest_distance:
                furthest_cubes.append(cube)
            if distance > furthest_distance:
                furthest_cubes = [cube]
                furthest_distance = distance

        current_cubes = furthest_cubes
        visited = furthest_cubes
        searching = True
        ordered_cubes = []
        while searching:
            print(current_cubes)
            available_connections = []
            #for each cube in current cubes:
            for cube in range(len(current_cubes)):
                #for each cube in the connected cubes:
                for connection in self.connections[cube]:
                    if connection not in visited:
                        available_connections.append(connection)
                        visited.append(connection)
            if len(available_connections) == 0:
                searching = False
                break
            current_cubes = available_connections
                

        return self.cubes
        """
        ordered_cubes = []
        cubes_magnitudes = {}
        for current_cube in self.cubes:
            furthest_point, closest_point = current_cube.return_landmark_points(screen_position)
            cube_to_screen = screen_position - furthest_point
            magnitude = np.sqrt(cube_to_screen.dot(cube_to_screen))
            cubes_magnitudes[current_cube] = magnitude
        for cube in sorted(cubes_magnitudes, key=cubes_magnitudes.get, reverse=False):
            ordered_cubes.append(cube)

        return ordered_cubes
        """

    def update(self):
        self.create_cubes()

    def rotate(self, rotation):
        self.rotation[0] = (self.rotation[0] + rotation[0]) % 360
        self.rotation[1] = (self.rotation[1] + rotation[1]) % 360
        self.rotation[2] = (self.rotation[2] + rotation[2]) % 360
        self.update()
        


        
