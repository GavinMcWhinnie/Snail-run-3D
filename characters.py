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
        
        eye_holder_1_position = cube.rotate_vector(np.array([32, -32, 60]), self.rotation)
        eye_holder_1 = cube.Cuboid(16, 16, 40, self.origin + eye_holder_1_position, self.rotation)
        self.cubes.append(eye_holder_1)
        
        eye_holder_2_position = cube.rotate_vector(np.array([-32, -32, 60]), self.rotation)
        eye_holder_2 = cube.Cuboid(16, 16, 40, self.origin + eye_holder_2_position, self.rotation)
        self.cubes.append(eye_holder_2)
        
        eye_1_position = cube.rotate_vector(np.array([32, -32, 100]), self.rotation)
        eye_1 = cube.Cube(20, self.origin + eye_1_position, self.rotation)
        self.cubes.append(eye_1)

        eye_2_position = cube.rotate_vector(np.array([-32, -32, 100]), self.rotation)
        eye_2 = cube.Cube(20, self.origin + eye_2_position, self.rotation)
        self.cubes.append(eye_2)

        shell_position = cube.rotate_vector(np.array([0, 140, 60]), self.rotation)
        shell = cube.Cuboid(120, 200, 200, self.origin + shell_position, self.rotation)
        self.cubes.append(shell)

    def return_sides(self):
        cubes_sides = []
        for cube in self.cubes:
            cubes_sides.append(cube.return_sides())
            
        return cubes_sides
            
        


        
