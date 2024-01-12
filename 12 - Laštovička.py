# Body
import math

# konstruktor a selektory:
def make_point(x=0, y=0): # výchozí hodnoty argumentů
    return ["point", x, y]

def get_point_x(point):
    return point[1]

def get_point_y(point):
    return point[2]

"""
>>> p = make_point(100, 200)
>>> get_point_x(p)
100
>>> get_point_y(p)
200
"""

def is_number(val):
    return type(val) == int or type(val) == float

"""
>>> is_number(1)
True
>>> is_number(1.0)
True
>>> is_number("1.0")
False
"""

# Typový predikát:
def is_point(val):
    return (type(val) == list
            and len(val) == 3
            and val[0] == "point"
            and is_number(val[1])
            and is_number(val[2]))


"""
>>> is_point(["point", 1, 2])
True
>>> is_point(["point", 1.0, 2])
True
>>> is_point(["point", "1", 2])
False
>>> is_point(1)
False
>>> is_point(["point", 1])
False
>>> is_point(["fract", 1, 2])
False
"""

# Mutátory:
def set_point_x(point, x):
    point[1] = x

def set_point_y(point, y):
    point[2] = y
    
"""
>>> p = make_point(0, 0)
>>> set_point_x(p, 100)
>>> set_point_y(p, 50)
>>> p
['point', 100, 50]
"""

def move_point(point, dx, dy):
    x = get_point_x(point)
    y = get_point_y(point)
    set_point_x(point, x + dx)
    set_point_y(point, y + dy)
    
"""
>>> p = make_point(100, 50)
>>> move_point(p, 50, 10)
>>> p
['point', 150, 60]
>>> p = make_point()
>>> p
['point', 0, 0]
>>> move_point(p, 50, 10)
>>> p
['point', 50, 10]
"""

def get_point_r(point):
    x = get_point_x(point)
    y = get_point_y(point)
    return math.sqrt((x ** 2) + (y ** 2))

"""
>>> get_point_r(make_point(3, 4))
5.0
"""

def signum(number):
    if number < 0:
        return -1
    elif number > 0:
        return 1
    else:
        return 0
    
def get_point_phi(point):
    x = get_point_x(point)
    y = get_point_y(point)
    if x > 0:
        return math.atan(y / x)
    elif x < 0:
        return math.pi + math.atan( y / x )
    else:
        return signum(y) * (math.pi / 2)
        
    
"""
>>> get_point_phi(make_point(3, 4))
0.9272952180016122
"""

def set_point_r_phi(point, r, phi):
    set_point_x(point, r * math.cos(phi))
    set_point_y(point, r * math.sin(phi))
    
"""
>>> p = make_point(0, 0)
>>> set_point_r_phi(p, 100, math.pi / 4)
>>> p
['point', 70.71067811865476, 70.71067811865474]
>>> get_point_phi(p)
0.7853981633974482
>>> math.pi / 4
0.7853981633974483
>>> get_point_r(p)
99.99999999999999
"""

def set_point_r(point, r):
    set_point_r_phi(point, r, get_point_phi(point))

def set_point_phi(point, phi):
    set_point_r_phi(point, get_point_r(point), phi)
    
"""
>>> p = make_point(1, 1)
>>> set_point_r(p, 2)
>>> p
>>> ['point', 1.4142135623730951, 1.414213562373095]
>>> set_point_phi(p, 0)
>>> p
['point', 2.0, 0.0]
"""
def rotate_point_origin(point, angle):
    phi = get_point_phi(point)
    set_point_phi(point, phi + angle)
    
"""
>>> p = make_point(100, 0)
>>> rotate_point_origin(p, math.pi / 2)
>>> p
['point', 6.123233995736766e-15, 100.0]
>>> rotate_point_origin(p, math.pi / 2)
>>> p
['point', -100.0, 1.2246467991473532e-14]
"""

def rotate_point(point, angle, center):
    cx = get_point_x(center)
    cy = get_point_y(center)
    move_point(point, -cx, -cy)
    rotate_point_origin(point, angle)
    move_point(point, cx, cy)
    
"""
>>> p = make_point(100, 0)
>>> c = make_point(50, 0)
>>> rotate_point(p, math.pi / 2, c)
>>> p
['point', 50.0, 50.0]
"""

