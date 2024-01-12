#Fce array_range(a, b) > (2, 10) => [2, 3, 4, 5, 6, 7, 8, 9]

def array_range(a, b):
    result = []
    for i in range(a, b):
        result = result + [i]
    return result
"""array_range(1,5)
    [1, 2, 3, 4]"""

# is_multiple(a, b) => (4, 2) => True (4, 3) => False
def is_multiple(a, b):
    return (a % b) == 0
"""is_multiple(10,5)
    True
    s_multiple(10,3)
    False"""

""" Erathosthenovo síto"""
# remove_multiples(2, [2, 3, 4, 5, 6, 7, 8, 9]) => [3, 5, 7, 9]
# array = [2, 3, 4, 5, 6, 7, 8, 9]
def remove_multiples(a, array):
    result = []
    for i in array:
        if not is_multiple(i, a):
            result = result + [i]
    return result

# get_primes(n) => (10) > [2, 3, 5, 7]
# Fce len = zjistí délku pole > len([1, 2, 3, 8, 9]) => 5

def get_primes(x):
    nums = array_range(2, x)
    result = []
    while len(nums) != 0:
        prime = nums [0]
        result = result + [prime]
        nums = remove_multiples(prime, nums)
    return result

#každé pole čísel je množina
# [1, 2] = [2, 1] = [1, 2, 2]
def is_member(x, array):
    for i in array:
        if x == i:
            return True
    return False

#is_subset([2, 1, 2], [2, 1])
def is_subset(array, sub_array):
    for i in array:
        if not is_member(i, sub_array):
            return False
    return True

#are_sets_equal([2, 1, 2], [2, 1]) => True

def are_sets_equal(a, b):
    return is_subset(a, b) and is_subset(b, a)

#sjednocení množin
def sets_union(set1, set2):
    return set1 + set2

#def are_sets_equal(set1, set2):

#rozdíl množin - sets_difference
def sets_difference(set1, set2):
    set3 = []
    for el in set1:
        if not is_member(el, set2):
            set3 = set3 + [el]
    return set3


#průnik množin - sets_intersect([1, 2, 3], [2, 3, 4])
def sets_intersect(set1, set2):
    return sets_difference(set1, sets_difference(set1, set2))


#Fce remove_duplicates([1, 2, 2])

#get_least = najde nejmenší prvek

# remove_element (el, array):

# sort(array)

















