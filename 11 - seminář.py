"""
x = [1, 2, 3]
x
[1, 2, 3]
x[2] = 4
x
[1, 2, 4]
"""
#destruktivní Fce - mění argumenty
def array_swap(array, index1, index2):
    temp = array[index1]
    array[index1] = array[index2]
    array[index2] = temp
    return array
"""
array_swap([1,2,3], 0,1)
[2, 1, 3]
"""
def array_swap2(array1, index1, index2):
    array2 = array1
    return array_swap(array2, index1, index2)


#nedestruktivní Fce - nemění argumenty
def array_swap3(array1, index1, index2):
    array2 = []
    for i in array1:
        array2 = array2 + [i]
    return array_swap(array2, index1, index2)
"""
x = [1,2,3]
array_swap3(x, 0,1)
[2, 1, 3]
x
[1, 2, 3]
"""

def reverse_array(array):
    result = []
    for i in array:
        result = [i] + result
    return result

def reverse_array2(array):
    l = len(array)
    for i in range (l // 2):
        array_swap(array, i, l - 1 - i)
        
"""
x = [1,2,3]
reverse_array(x)
[3, 2, 1]
x
[1, 2, 3]
"""


def is_palindrom(array):
    return reverse_array(array) == array
"""
x = [1,2,2,1]
is_palindrom(x)
True
is_palindrom([1,2,3,2,1])
True
is_palindrom([1,2,3,2,1,0])
False
"""

def array_copy(array):
    new_array = []
    for i in array:
        new_array = new_array + [i]
    return new_array

def array_copy2(array):
    new_array = []
    new_array = new_array + array
    return new_array

def array_copy3(array):
    result = []
    for el in array:
        result += [el]
    return result

def array_copy4(array):
    result = [none] * len(array)
    for i in range(len(array)):
        result[i] = array[i]
    return result

"""
x = [1,2,2,1]
b = array_copy(x)
b
[1, 2, 2, 1]
x
[1, 2, 2, 1]
x == b
True
x is b
False
"""
def array_range(a, b):
    result = [None] * (b - a)
    for i in range(b - a):
        result[i] = i
    return result

def is_multiple(x, y):
    return (x % y) == 0


def delete_multiples_from(num, array, index):
    for i in range (index, len(array)):
        el = array[i]
        if el != None and is_multiple(el, num):
            array[i] = None


        














