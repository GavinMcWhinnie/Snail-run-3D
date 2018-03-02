import numpy as np
import cube

class Snail():

    def __init__(self, origin, rotation=None):

        self.origin = np.array(origin)
        if rotation == None:
            rotation = [0, 0, 0]
        self.rotation = np.array(rotation)
        self.create_cubes()

    def create_cubes(self):
        self.cubes = []

        head = cube.Cube(40, self.origin, self.rotation)
        self.cubes.append(head)
        
        eye_holder_1_position = cube.rotate_vector(np.array([36, -36, -60]), self.rotation)
        eye_holder_1 = cube.Cuboid(16, 16, 40, self.origin + eye_holder_1_position, self.rotation)
        self.cubes.append(eye_holder_1)
        
        eye_holder_2_position = cube.rotate_vector(np.array([-18, -18, 25]), self.rotation)
        eye_holder_2 = cube.Cuboid(4, 4, 10, self.origin + [-18, -18, 25], self.rotation)
        self.cubes.append(eye_holder_2)
        
        eye_1_position = cube.rotate_vector(np.array([17.5, 17.5, 32.5]), self.rotation)
        eye_1 = cube.Cube(5, self.origin + eye_1_position, self.rotation)
        self.cubes.append(eye_1)

        eye_2_position = cube.rotate_vector(np.array([-17.5, -17.5, 32.5]), self.rotation)
        eye_2 = cube.Cube(5, self.origin + eye_2_position, self.rotation)
        self.cubes.append(eye_2)

    def return_sides(self):
        cubes_sides = []
        for cube in self.cubes:
            cubes_sides.append(cube.return_sides())
            
        return cubes_sides
            
        


        
