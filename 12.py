import math

def is_number(num):
    return type(num) == int or type(num) == float

def is_point(val):
    return (type(val) == list
            and len(val) == 3
            and is_number(val[1])
            and is_number(val[2]))


def get_point_x(point):
    return point[1]

def get_point_y(point):
    return point[2]

def make_point(x=0, y=0):
    return ["point", x, y]


def move_point(point, dx, dy):
    x = get_point_x(point)
    y = get_point_y(point)
    make_point_x(point, x + dx)
    make_point_x(point, y + dy)
    
def get_point_r(point):
    x = get_point_x(point)
    y = get_point_y(point)
    return math.sqrt((x ** 2) + (y ** 2))


def get_point_phi(point):
    x = get_point_x(point)
    y = get_point_y(point)
    if x > 0:
        return math.atan(y / x)
    elif x < 0:
        return math.pi + math.atan(y / x)
    else:
        return signum(y) + (math.py / 2)

def set_point_r_phi(point, r, phi):
    set_point_x(point, r * math.cos(phi))
    set_point_y(point, r * math.sin(phi))

def set_point_r(point, r):
    set_point_r_phi(point, r, get_point_phi(point))

def rotate_point_origin(point, math.pi / 2):
    phi = get_point_phi(point)
    set_point_phi(point, phi + angle)

def rotate_point(point, angle, center):
    cx = get_point_x(center)
    xy = get_point_y(center)

        

































    
    

