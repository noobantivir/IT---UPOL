#3.2

def get_last_digit(x):
    return x % 10
"""pomocná Fce na zjištění poslední číslice"""

def remove_last_digit(x):
    return x // 10
"""odebere poslední cifru"""

def get_digits(number):
    result = []
    while number != 0:
        temp = get_last_digit(number)
        result = result + [temp]
        number = remove_last_digit(number)
        print(number)
    return result
"""ze zadaného čísla získá pole o jednotlivých cifrách"""
#3.3
def get_dividers(number):
    result = []
    for i in range(1, number + 1):
        if (number % i) == 0:
            result = result + [i]
    return result

#3.5
def get_number_from_digits(numbers):
    result = 0
    for i in numbers:
        result = result * 10
        result = result + i
    return result
"""po zadání čísel, nám vznikne číslo"""

#3.6
def array_sum(numbers):
    result = 0
    for i in numbers:
        result = result + i
        print(i)
    return result
"""součet prvků pole"""


#3.7
def get_digit_sum(number):
    return array_sum(get_digits(number))
"""ciferný součet čísla"""

#3.7b
def get_digit_sum_alternative(number):
    result = 0
    while number != 0:
        last_digit = number % 10
        result = last_digit + result
        number = number // 10
        print(last_digit, number, result)
    return result


#3.8 wtf je cifrace???
"""def digital_root(number):"""
    

#3.9
def reverse_array(number):
    return get_digits(get_number_from_digits(number))

#3.10
def are_arrays_equal(array1, array2):
    return array1 == array2

#3.11 ???? + 3.12
#def is_array_palindrom(numbers):

#3.13
def array_mult(number):
    result = 1
    for i in number:
        result = result * i
        print(result, i)
    return result

#3.14
def number_dividers(number):
    result = []
    for i in range(1, number + 1):
        if number % i == 0:
            result = result + [i]
        print(i, result)
    return result
"""zadanému číslu najde všechny dělitele"""


#3.14 ??
"""def prime_factor(number):
    result = []
    for i in range(1, number + 1):
        if number % i == 0:
            result = result + [i]
            number = number // i
            print(number, i)
    return result


def prime_factor(number):
    result = []
    while number != 1:
        number = number // divider
        result = result + [divider]
    return result """

#3.15
#pomocná Fce
def is_member(number, array):
    for i in array:
        if number == i:
            return True
    return False
""" patří zadané číslo do pole prvků?"""

#def is_subarray(array1, array2):
def is_subbaray(sub_array, array):
    for i in sub_array:
        if not is_member(i, array):
            return False
    return True
"""zjistí zda array1 je podmnožinou array2"""

#3.16
def is_in_both_arrays(array1, array2):
    result = []
    previous_num = 0
    for i in array1:
        if is_member(i, array2) and previous_num != i:
            previous_num = i
            result = result + [i]
            print(previous_num)
    return result
"""Fce najde společné hodnoty obou polí,
se vzestupně uspořádanými prvky a bez duplicitních hodnot. """



















