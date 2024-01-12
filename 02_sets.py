# Každé pole čísel chápeme jako množinu.
#
# Nezajímá nás pořadí a ani duplicita prvků.
# Následující tři pole reprezentují tutéž množinu. 
# [1, 2]
# [2, 1]
# [1, 2, 2]

# Náležení prvku do množiny:
def is_member(val, array):
    for el in array:
        if el == val:
            return True
        # print(el)
    return False

"""
>>> is_member(1, [2, 1])
True
>>> is_member(3, [2, 1])
False
"""

# Podmnožinovost:
def is_subset(set1, set2):
    for el in set1:
        if not is_member(el, set2):
            return False
        # print(el)
    return True
    
"""
>>> is_subset([2, 1, 2], [2, 1])
True
>>> is_subset([2, 1, 2], [2, 1, 3])
True
>>> is_subset([2, 1, 4, 2], [2, 1, 3])
False
"""

# Rovnost množin:
def are_sets_equal(set1, set2):
    return is_subset(set1, set2) and is_subset(set2, set1)

"""
>>> are_sets_equal([2, 1, 2], [2, 1])
True
>>> are_sets_equal([2, 1, 2], [2, 1, 3])
False
>>> are_sets_equal([2, 1, 4, 2], [2, 1])
False
"""

# Sjednocení:
def sets_union(set1, set2):
    return set1 + set2

"""
>>> sets_union([1, 2], [2, 3])
[1, 2, 2, 3]
>>> are_sets_equal(sets_union([1, 2], [2, 3]), [1, 2, 3])
True
"""

# Rozdíl:
def sets_difference(set1, set2):
    set3 = []
    for el in set1:
        if not is_member(el, set2):
            set3 = set3 + [el]
    return set3

"""
>>> sets_difference([1, 2, 3, 2], [3, 2, 2])
[1]
"""

# Průnik:
def sets_intersect(set1, set2):
    return sets_difference(set1, sets_difference(set1, set2))
    
"""
>>> sets_intersect([1, 2, 3], [2, 3, 4])
[2, 3]
"""

