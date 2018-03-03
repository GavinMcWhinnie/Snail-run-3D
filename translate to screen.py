import numpy as np

#inputs:
#screen position
#screen direction
#viewer distance
#3D point

#screen_position = np.array([100,100,100])
#screen_direction = np.array([-1,-1,-1])
#viewer_distance = 50
#_3D_point = np.array([0,0,100])

def translate(_3D_point, screen_position, screen_direction, viewer_distance):

    ## screen rotation is not yet available
    ## prints error if point not visible - what else should happen instead?
    
    ###### step 1 ######
    #work out where viewer is

    magnitude_of_direction = np.sqrt(screen_direction.dot(screen_direction))
    viewer_vector = screen_direction * (viewer_distance / -magnitude_of_direction)

    viewer_position = viewer_vector + screen_position

    ###### step 2 ######
    #create line from point to viewer

    point_to_viewer = viewer_position - _3D_point


    ###### step 3 ######
    #create plane that screen rests on

    a, b, c = screen_direction

    d = -(screen_direction.dot(screen_position))

    viewer_side_of_plane = abs(viewer_position.dot(screen_direction) + d) / (viewer_position.dot(screen_direction) + d)

    if (_3D_point.dot(screen_direction) + d) * viewer_side_of_plane == abs(_3D_point.dot(screen_direction) + d):
        print("ERROR: point not visible")
        ######### point cannot be shown as it is on the same side of screen as viewer ########
    else:
        pass
        ##point is visible

    ###### step 4 ######
    #find out where line intersects the screen

    #ax + by + cz + d = 0
    #a(p + td) + b(q + te) + c(r + tf) + d = 0
    #ap + atd + bq + bte + cr + ctf + d = 0
    #ap + bq + cr + d = -atd - bte - ctf = 0
    #-t (ad + be + cf) = ap + bq + cr + d
    #t = -(ap + bq + cr + d)/(ad + be + cf)
    #t = -(a, b, c) . (p, q, r) + d / (a, b, c) . (d, e, f)

    t = -((screen_direction.dot(_3D_point) + d) / screen_direction.dot(point_to_viewer))

    intersection = _3D_point + (point_to_viewer * t)
    
    ###### step 5 ######

    ratio_for_x_axis = 1 / np.sqrt(a**2 + b**2 + c**2)

    x_axis = np.array([-b * ratio_for_x_axis, a * ratio_for_x_axis, 0])

    #ax + by + cz = 0
    #-cz = ax + by
    #z = -(ax + by)/c

    p = -((abs(c)/c) * a)
    q = -((abs(c)/c) * b)
    r = -(a * p + b * q)/c

    y_axis = np.array([p, q, r])

    magnitude_of_y_axis = np.sqrt(y_axis.dot(y_axis))
    ratio_for_y_axis = 1 / magnitude_of_y_axis

    y_axis = y_axis * ratio_for_y_axis

    ###### step 6 ######

    vector_on_plane = intersection - screen_position


    #vector_on_plane = [l, m, n]
    #x_axis = [a, b, 0]
    #y_axis = [d, e, f]

    #[l]   [xa]   [yd]
    #[m] = [xb] + [ye]
    #[n]   [0 ]   [yf]

    y = vector_on_plane[2] / y_axis[2]

    #l = xa + yd
    #l - yd = xa
    #x = (l - yd)/a

    
    x = (vector_on_plane[0] - y * y_axis[0]) / x_axis[0]

    _2D_vector = np.array([round(x,2), round(y,2)])

    return _2D_vector

if __name__ == "__main__":
    screen_position = np.array([100,100,100])
    screen_direction = np.array([-1,-1,-1])
    viewer_distance = 50
    _3D_point = np.array([0,0,100])

    print(translate(_3D_point, screen_position, screen_direction, viewer_distance))
