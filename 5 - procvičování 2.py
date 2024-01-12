#3.2
def get_digits(number):
    result = []
    while number != 0:
        last_digit = number % 10
        result = result + [last_digit]
        number = number // 10
    return result

#3.3
def get_dividers(number):
    result = []
    for divider in range(1, number + 1):
        if number % divider == 0:
            result = result + [divider]
    return result
#3.5
def get_number_from_digits(array):
    result = 0
    for digit in array:
        result = result * 10 + digit
    return result

#3.6
def array_sum(array):
    result = 0
    for digit in array:
        result = result + digit
    return result
#3.7
def get_digit_sum(number):
    result = 0
    while number != 0:
        last_digit = number % 10
        result = result + last_digit
        number = number // 10
    return result
#3.9
def reverse_array(array):
    return get_digits(get_number_from_digits(array))

#3.10
def sub_array(number, array):
    for i in array:
        if number == i:
            return True
    return False

def are_arrays_equal(array1, array2):
    return array1 == array2
#3.11
def is_palindrom(array):
    if reverse_array(array) == array:
        return True
    return False

#3.13
def array_multi(array):
    result = 1
    for i in array:
        result = result * i
    return result
#3.14
def prime_fact(number):
    result = []
    while number != 1:
        for i in range(2, number + 1):
            if number % i == 0:
                number = number // i
                result = result + [i]
                print(result, i)
    return result

#součet, rozdíl,
def add_arrays(array1, array2):
    return array1 + array2

def deduct_arrays(array1, array2):
    result = []
    for number in array1:
        if not is_member(number,array2):
            result = result + [number]
    return result


def smallest_num(array):
    for i in array:
        if i < temp:
            smallest = i
    return smallest
