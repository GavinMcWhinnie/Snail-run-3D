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

def rotate_vector(vector, rotation):
    x_rotate = vector.dot(create_x_rotation(rotation[0]))
    y_rotate = x_rotate.dot(create_y_rotation(rotation[1]))
    z_rotate = y_rotate.dot(create_z_rotation(rotation[2]))
    return z_rotate


#########################################################

class Cube():

    def __init__(self, size, origin, color, rotation=None):
        self.origin = np.array(origin)
        self.size = size
        self.color = color
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
        self.sides = []
        self.update_points()
        for magic_number in self.magic_numbers:
            for x in range(0, 3):
                self.sides.append([self.points[magic_number],self.points[magic_number ^ (2 ** x)]])

    def update_faces(self):
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
    
    def return_sides(self):
        return self.sides, self.color

    def return_faces(self, screen_position):
        highest_magnitude = 0
        furthest_point = 0
        for point in self.points:
            point_to_screen = screen_position - point
            magnitude = np.sqrt(point_to_screen.dot(point_to_screen))
            if magnitude > highest_magnitude:
                highest_magnitude = magnitude
                furthest_point = point
        visible_faces = []
        for face in self.faces:
            try:
                face.index(furthest_point)
            except ValueError:
                visible_faces.append(face)

        return visible_faces, self.color

    def rotate(self, rotation):
        self.rotation[0] = (self.rotation[0] + rotation[0]) % 360
        self.rotation[1] = (self.rotation[1] + rotation[1]) % 360
        self.rotation[2] = (self.rotation[2] + rotation[2]) % 360

class Cuboid():

    def __init__(self, width, height, breadth, origin, color, rotation=None):
        self.origin = np.array(origin)
        self.width = width
        self.height = height
        self.breadth = breadth
        self.color = color
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

    def update_sides(self):
        self.sides = []
        self.update_points()
        for magic_number in self.magic_numbers:
            for x in range(0, 3):
                self.sides.append([self.points[magic_number],self.points[magic_number ^ (2 ** x)]])

    def update_faces(self):
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

    def return_sides(self):
        return self.sides, self.color

    def return_faces(self, screen_position):
        highest_magnitude = 0
        furthest_point = 0
        for point in self.points:
            point_to_screen = screen_position - point
            magnitude = np.sqrt(point_to_screen.dot(point_to_screen))
            if magnitude > highest_magnitude:
                highest_magnitude = magnitude
                furthest_point = point
        visible_faces = []
        for face in self.faces:
            try:
                face.index(furthest_point)
            except ValueError:
                visible_faces.append(face)

        return visible_faces, self.color

    def rotate(self, rotation):
        self.rotation[0] = (self.rotation[0] + rotation[0]) % 360
        self.rotation[1] = (self.rotation[1] + rotation[1]) % 360
        self.rotation[2] = (self.rotation[2] + rotation[2]) % 360

#########################################################

if __name__ == "__main__":
    example = Cube(10,[0,0,0])

