# Práce s desetinnými čísly je obecně nepřesná. 
"""
>>> 0.1 + 0.1 + 0.1 == 0.3
False
>>> 0.1 + 0.1 + 0.1
0.30000000000000004
"""

# Desetinné číslo vyjádřené zlomkem:
"""
>>> x = 0.1
>>> x.as_integer_ratio()
(3602879701896397, 36028797018963968)
"""

# Převod desetinného čísla na řetězec se zadaným platým počtem cifer:
"""
>>> format(0.1, ".55g")
'0.1000000000000000055511151231257827021181583404541015625'
"""

# Více: https://docs.python.org/3/tutorial/floatingpoint.html

def get_distance(x, y):
    return abs(x - y)
    
"""
>>> get_distance(0.1 + 0.1 + 0.1, 0.3)
5.551115123125783e-17
"""
EPSILON = 1e-10

def are_similar(x, y, epsilon=EPSILON):
    return get_distance(x, y) < epsilon

"""
>>> are_similar(0.1 + 0.1 + 0.1, 0.3, 1e-10)
True
"""

def sqrt_step(a, x):
    return (1 / 2) * (x + (a / x))

"""
>>> sqrt_step(2, 2)
1.5
>>> sqrt_step(2, 1.5)
1.4166666666666665
>>> sqrt_step(2, 1.4166666666666665)
1.4142156862745097
"""
def my_sqrt(a, n):
    x = a
    for i in range(n):
        x = sqrt_step(a, x)
        print(x, get_distance(x ** 2, a))
    return x
        
# my_sqrt

def my_sqrt2(a, epsilon=EPSILON):
    """Vrátí druhou odmocninu čísla."""
    x1 = a
    x2 = sqrt_step(a, x1)
    while not are_similar(x1, x2, epsilon):
        x1 = x2
        x2 = sqrt_step(a, x1)
        # print(x1, get_distance(x1, x2))
    return x1

"""
>>> get_distance(my_sqrt2(2), 2 ** 0.5)
1.5947243525715749e-12
"""
def get_fib(n):
    x0 = 0
    x1 = 1
    for i in range(n):
        x2 = x0 + x1
        x0 = x1
        x1 = x2
    return x0

"""
>>> get_fib(5)
5
>>> get_fib(6)
8
"""

def get_golden_ratio(n):
    return get_fib(n + 1) / get_fib(n)
    
# golden_ratio fib(n + 1) / fib(n)
# fib: 0, 1, 1, 2, 3, 5, 8
# 1.618033988749...

def get_next_fib_pair(pair):
    return [pair[1], pair[0] + pair[1]]

"""
>>> get_next_fib_pair([0, 1])
[1, 1]
>>> get_next_fib_pair([1, 1])
[1, 2]
>>> get_next_fib_pair([1, 2])
[2, 3]
>>> get_next_fib_pair([2, 3])
[3, 5]
"""

def estimate_golden_ratio(pair):
    return pair[1] / pair[0]

"""
>>> estimate_golden_ratio([1, 2])
2.0
>>> estimate_golden_ratio([2, 3])
1.5
"""

def get_golden_ratio2(epsilon=EPSILON):
    pair = get_next_fib_pair([0, 1])
    next_pair = get_next_fib_pair(pair)
    estimate = estimate_golden_ratio(pair)
    next_estimate = estimate_golden_ratio(next_pair)
    while not are_similar(estimate,
                          next_estimate,
                          epsilon):
        print(pair, next_pair, estimate, next_estimate)
        next_next_pair = get_next_fib_pair(next_pair)
        pair = next_pair
        next_pair = next_next_pair
        next_next_estimate = estimate_golden_ratio(next_next_pair)
        estimate = next_estimate
        next_estimate = next_next_estimate
    return next_estimate


# Úkol: Spočítejte přibližně pi pomocí Wallisova součinu:
# https://en.wikipedia.org/wiki/Wallis_product
#
# a) Spočítejte součin zadaného počtu zlomků.
# b) Spočítejte nejprve celočíselného čitatele a jmenovatele
#    pro zadaný počet součinů a teprve poté proveďte nepřesný podíl.
# c) Liší se výsledky?
