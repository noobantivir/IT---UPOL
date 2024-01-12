
EPSILON = 1e-10

def are_similar (x, y, e):
    return abs(x - y) < e

"""
are_similar(0.1 + 0.1 + 0.1, 0.3, 1e-10)
True
"""


def get_distance(x, y):
    return x - y
"""
get_distance(0.1 + 0.1 + 0.1, 0.3)
5.551115123125783e-17
"""


def sqrt_step(a, x):
    return (1/2) * (x + (a / x))

def my_sqrt(a, n):
    x = a
    for i in range(n):
        x = sqrt_step(a, x)
    return x

def my_sqrt2(a, e = E):
    x1 = a
    x2 = sqrt_step(a, x1)
    while not are_similar(x1, x2, e):
        x2 = sqrt_step(a, x1)
        x1 = x2
    return x1
"""
my_sqrt2(8)
4.5
my_sqrt2(4)
2.5
"""

def fib_num(n):
    x0 = 0
    x1 = 1
    for i in range(n):
        x2 = x0 + x1
        x0 = x1
        x1 = x2
        # print(x0, x1, x2)
    return x0
"""
fib_num(8)
21
"""
    
def golden_ratio(num):
    return fib_num(num + 1) / fib_num(num)
"""
golden_ratio(3)
1.5
golden_ratio(11)
1.6179775280898876
"""

def get_next_fib_pair(pair):
    return [pair[1], pair[0] + pair[1]]
"""
get_next_fib_pair([0,1])
[1, 1]
get_next_fib_pair([1, 1])
[1, 2]
"""

def estimate_golden_ratio(pair):
    return pair[1] / pair[0]
"""
estimate_golden_ratio([2, 1])
0.5
"""


def get_golden_ratio2(epsilon = EPSILON):
    pair = get_next__fib_pair([0, 1])
    next_pair = get_next_fib_pair(pair)
    estimate = estimate_golden_ratio(pair)
    next_estimate = estimate_golden_ratio(next_pair)
    while not are_similar(estimate,
                          next_estimate,
                          epsilon):
        next_next_pair = get_next_fib_pair(next_pair)
        pair = next_pair
        next_pair = next_next_pair
        next_next_estimate = estimate_golden_ratio(next_next_pair)
        estimate = next_estimate
        next_estimate
        pass










