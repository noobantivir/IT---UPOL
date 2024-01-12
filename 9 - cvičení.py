##def gcd(a, b):
##    if a > b:
##        while b != 0:
##            c = b
##            b = a % b
##            a = c
##        return a
##    else:
##        while a != 0:
##            c = a
##            a = b % a
##            b = c
##        return b

# konstruktor
def make_fract(numerator, denominator):
    return ["fract", numerator, denominator]

# selektory:
def get_num(fract):
    return fract[1]

def get_den(fract):
    return fract[2]


def are_fracts_equal(fract1, fract2):
    num1 = get_num(fract1)
    den1 = get_den(fract1)
    num2 = get_num(fract2)
    den2 = get_den(fract2)
    return num1 * den2 == num2 * den1
"""
are_fracts_equal(make_fract(2,4),make_fract(1,2))
True
"""

def add_fracts(fract1, fract2):
    num1 = get_num(fract1)
    den1 = get_den(fract1)
    num2 = get_num(fract2)
    den2 = get_den(fract2)
    if den2 == den1:
        return make_fract(num1 + num2, den1)
    else:
        return make_fract((num1 * den2) + (num2 * den1), den1 * den2)
"""
add_fracts(make_fract(2,4),make_fract(1,2))
['fract', 8, 8]
"""


def mult_fracts(fract1, fract2):
    num1 = get_num(fract1)
    den1 = get_den(fract1)
    num2 = get_num(fract2)
    den2 = get_den(fract2)
    return make_fract((num1 * num2), (den1 * den2))

"""
mult_fracts(make_fract(2,4),make_fract(1,2))
['fract', 2, 8]
"""

def get_gcd(a, b):
    while b != 0:
        c = b
        b = a % b
        a = c
    return a

"""
gcd(2,4)
2
gcd(4,2)
2
gcd(6,8)
2
gcd(18,24)
6
"""
            
def reduce_fract(fract1):
    num1 = get_num(fract1)
    den1 = get_den(fract1)
    gcd = get_gcd(num1, den1)
    return make_fract(num1 // gcd, den1 // gcd)
"""
reduce_fract(make_fract(2,4))
['fract', 1, 2]
"""
def invert_add(fract1):
    return make_fract(- get_num(fract1), get_den(fract1))
"""
invert_add(make_fract(2,5))
['fract', -2, 5]
"""

def sub_fracts(fract1, fract2):
    return add_fracts(fract1, invert_add(fract2))
"""
sub_fracts(make_fract(2,5), make_fract(1,8))
['fract', 11, 40]
"""

def invert_mult(fract):
    num1 = get_num(fract)
    den1 = get_den(fract)
    return make_fract(den1, num1)
"""
invert_mult(make_fract(2,4))
['fract', 4, 2]
"""

def div_fracts(fract1, fract2):
    return mult_fracts(fract1, invert_mult(fract2))
"""
div_fracts(make_fract(2,5),make_fract(5,1))
['fract', 2, 25]
"""
def fract_to_ingeter(fract):
    return get_num(fract) // get_den(fract)
"""
fract_to_ingeter(make_fract(10,5))
2
"""


def fract_to_decimal(fract, n):
    integer = fract_to_integer(fract)
    rest = sub_fracts(fract, make_fract(integer, 1))
    mult_rest = mult_fracts(rest, make_fract(10 ** n, 1))
    return str(integer) + "."


def sqrt(fract, n):
    res = fract
    for i in range(n):
        res = mult_fracts(make_fract(1, 2),
                          add_fracts(res,
                                     div_fracts(fract, res)))
    return res














