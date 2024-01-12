#4 cvičení (2. zápočťák)

#print_digits(123) = 3,2,1


def get_last_digit(a):
    return a % 10
"""pomocná Fce pro print_digits"""


def remove_last_digit(b):
    return (b // 10)
"""pomocná Fce pro print_digits"""


def print_digits(x):
    while x != 0:
        result = get_last_digit (x)
        x = remove_last_digit (x)
    return result

def get_digits(x):
    empty = []
    while x > 0:
        empty = [get_last_digit(x)] + empty
        x = remove_last_digit(x)
    print(empty)

#is_divisor (2, 6) => True
""" get_dividers(6)
[1, 2, 3, 6]"""

#get_evens(8) => [0, 2, 4, 6, 8]
def get_evens(x):
    result = []
    for i in range(1, x + 1):
        if x % x == 0:
            result = [x] + result
            x = x - 1
            return result
        else:
            return x - 1

        
def append_digit(number, digit):
    return (number * 10) + digit


def get_number_from_digits(digits):
    number = 0
    for i in range(len(digits)):
        digit = digits[i]
        number = append_digit(number, digit)
    return number

#array_sum([1, 2, 1, 3]) –> 7

#def array_sum(digit):
    

















