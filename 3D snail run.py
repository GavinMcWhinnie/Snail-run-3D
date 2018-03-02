import pygame
import numpy as np

def create_x_rotation(rotX):
    rotX = np.radians(rotX)
    r = np.array([[1,0,0],
                  [0, np.cos(rotX),-np.sin(rotX)],
                  [0, np.sin(rotX),np.cos(rotX)]])
    return r

def create_y_rotation(rotY):
    rotY = np.radians(rotY)
    r = np.array([[np.cos(rotY),0,np.sin(rotY)],
                  [0,1,0],
                  [-np.sin(rotY),0,np.cos(rotY)]])
    return r

def create_z_rotation(rotZ):
    rotZ = np.radians(rotZ)
    r = np.array([[np.cos(rotZ),-np.sin(rotZ),0],
                  [np.sin(rotZ),np.cos(rotZ),0],
                  [0,0,1]])
    return r

def rotate_vector(vector, rotX, rotY, rotZ):
    x_rotate = vector.dot(create_x_rotation(rotX))
    y_rotate = x_rotate.dot(create_y_rotation(rotY))
    z_rotate = y_rotate.dot(create_z_rotation(rotZ))
    return z_rotate

#########################################################

class Cube():

    def __init__(self, size, origin, rotX, rotY, rotZ):
        self.origin = np.array(origin)
        self.size = size
        self.rotX = rotX
        self.rotY = rotY
        self.rotZ = rotZ
        self.update_sides()

    def update_points(self):
        self.points = []
        for point in range(0, 8):
            new_vector = np.array([int(x) - 0.5 for x in format(point, "b").zfill(3)])
            scaled = new_vector * self.size * 2
            rotated = rotate_vector(scaled, self.rotX, self.rotY, self.rotZ)
            shifted = rotated + self.origin
            self.points.append(shifted)

    def update_sides(self):
        self.sides = []
        self.update_points()
        magic_numbers = [0, 3, 5, 6]
        for magic_number in magic_numbers:
            for x in range(0, 3):
                self.sides.append([self.points[magic_number],self.points[magic_number ^ (2 ** x)]])

    def rotate(self, x,y,z):
        self.rotX = (self.rotX + x) % 360
        self.rotY = (self.rotY + y) % 360
        self.rotZ = (self.rotZ + z) % 360

if __name__ == "__main__":
    example = Cube(10,[0,0,0], 0, 0, 0)

