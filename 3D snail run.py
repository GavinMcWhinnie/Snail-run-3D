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

class canvas():

    def __init__(self, width, height):

        self.width = width
        self.height = height


