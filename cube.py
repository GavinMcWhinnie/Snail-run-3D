import numpy as np
import colorsys

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

def rotate_vector(vector, rotation):
    x_rotate = vector.dot(create_x_rotation(rotation[0]))
    y_rotate = x_rotate.dot(create_y_rotation(rotation[1]))
    z_rotate = y_rotate.dot(create_z_rotation(rotation[2]))
    return z_rotate


#########################################################

class Cube():

    def __init__(self, size, origin, colour, rotation=None):
        self.origin = np.array(origin)
        self.size = size
        self.colour = colour
        if type(rotation) == type(None):
            rotation = [0, 0, 0]
        self.rotation = np.array(rotation)
        self.magic_numbers = [0, 3, 5, 6]
        self.update_sides()
        self.update_faces()

    def update_points(self):
        self.points = []
        for point in range(0, 8):
            new_vector = np.array([int(x) - 0.5 for x in format(point, "b").zfill(3)])
            scaled = new_vector * self.size * 2
            rotated = rotate_vector(scaled, self.rotation)
            shifted = rotated + self.origin
            self.points.append(shifted)

    def update_sides(self):
        self.update_points()
        self.sides = []
        for magic_number in self.magic_numbers:
            for x in range(0, 3):
                self.sides.append([self.points[magic_number],self.points[magic_number ^ (2 ** x)]])

    def update_faces(self):
        self.update_sides()
        self.faces = []
        magics = self.magic_numbers
        for x in range(len(magics)):
            magic = magics[0]
            del magics[0]
            for remaining_magic in magics:
                if remaining_magic ^ magic == 6:
                    self.faces.append([self.points[x] for x in [magic, magic ^ 2, remaining_magic, remaining_magic ^ 2]])
                else:
                    self.faces.append([self.points[x] for x in [magic, magic ^ 1, remaining_magic, remaining_magic ^ 1]])
        self.magic_numbers = [0, 3, 5, 6]

    def return_landmark_points(self, screen_position):
        highest_magnitude = 0
        furthest_point = 0
        for point in range(len(self.points)):
            point_to_screen = screen_position - self.points[point]
            magnitude = np.sqrt(point_to_screen.dot(point_to_screen))
            if magnitude > highest_magnitude:
                highest_magnitude = magnitude
                furthest_point = point
        closest_point = abs(furthest_point - 7)
        return furthest_point, closest_point
    
    def return_sides(self, screen_position):
        furthest_point, closest_point = self.return_landmark_points(screen_position)
        visible_sides = []
        for adjacent_point in range(0, 3):
            adjacent_point = closest_point ^ (2 ** adjacent_point)
            for visible_side in range(0, 3):
                visible_sides.append((self.points[adjacent_point], self.points[adjacent_point ^ (2 ** visible_side)]))
        return visible_sides

    def return_faces(self, screen_position, darkness):
        furthest_point, closest_point = self.return_landmark_points(screen_position)
        visible_faces = []
        for face in self.faces:
            for point in face:
                if (point == self.points[closest_point]).all():
                    average_point = np.array([0.0,0.0,0.0])
                    for point in face:
                        average_point += point
                    average_point /= 4
                    brightness = (average_point[2] - self.origin[2]) / self.size
                    color = colorsys.rgb_to_hls(self.colour[0],self.colour[1],self.colour[2])
                    lightness = (color[1] + brightness * 100 - darkness)
                    if lightness < -127.5:
                        lightness = -127.5
                    elif lightness > 127.5:
                        lightness = 127.5
                    color = (color[0], lightness, color[2])
                    color = colorsys.hls_to_rgb(color[0], color[1], color[2])
                    color = (int(abs(color[0])), int(abs(color[1])), int(abs(color[2])))
                    visible_faces.append((face,color))

        return visible_faces

    def rotate(self, rotation):
        self.rotation[0] = (self.rotation[0] + rotation[0]) % 360
        self.rotation[1] = (self.rotation[1] + rotation[1]) % 360
        self.rotation[2] = (self.rotation[2] + rotation[2]) % 360
        self.update_faces()

class Cuboid(Cube):

    def __init__(self, width, height, breadth, origin, colour, rotation=None):
        self.origin = np.array(origin)
        self.width = width
        self.height = height
        self.breadth = breadth
        self.colour = colour
        if type(rotation)== type(None):
            rotation = [0, 0, 0]
        self.rotation = np.array(rotation)
        self.magic_numbers = [0, 3, 5, 6]
        self.update_sides()
        self.update_faces()

    def update_points(self):
        self.points = []
        for point in range(0, 8):
            new_vector = np.array([int(x) - 0.5 for x in format(point, "b").zfill(3)])
            scaled = new_vector * np.array([self.width, self.height, self.breadth])
            rotated = rotate_vector(scaled, self.rotation)
            shifted = rotated + self.origin
            self.points.append(shifted)

    def return_faces(self, screen_position, darkness):
        furthest_point, closest_point = self.return_landmark_points(screen_position)
        visible_faces = []
        for face in self.faces:
            for point in face:
                if (point == self.points[closest_point]).all():
                    average_point = np.array([0.0,0.0,0.0])
                    for point in face:
                        average_point += point
                    average_point /= 4
                    brightness = (average_point[2] - self.origin[2]) / (self.height / 2)
                    color = colorsys.rgb_to_hls(self.colour[0],self.colour[1],self.colour[2])
                    lightness = (color[1] + brightness * 100 - darkness)
                    if lightness < -127.5:
                        lightness = -127.5
                    elif lightness > 127.5:
                        lightness = 127.5
                    color = (color[0], lightness, color[2])
                    color = colorsys.hls_to_rgb(color[0], color[1], color[2])
                    color = (int(abs(color[0])), int(abs(color[1])), int(abs(color[2])))
                    visible_faces.append((face,color))

        return visible_faces

#########################################################

if __name__ == "__main__":
    RED = (255, 0, 0)
    example = Cube(10,[0,0,0],RED)

