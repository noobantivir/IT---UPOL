# Jen seřazené pole bez duplicit chápeme jako množinu.
# Každá konečná množina je reprezentována jediným polem.
# Například: [1, 2, 5, 8]

# Nejmenší prvek pole:
def get_least(array):
    pass

"""
>>> get_least([2, 3, 1, 2])
1
"""

# Odstranění prvku z pole:
def remove_element(el, array):
    pass

"""
>>> remove_element(1, [1, 2, 1, 3])
[2, 3]
"""

# Seřadí pole a navíc odstraní duplicity:
def sort(array):
    pass

"""
>>> sort([3, 1, 2, 1])
[1, 2, 3]
"""


# Doplňte predikáty a funkce pracující s množinami.

# Využijte faktu, že prvky v pole jsou seřazeny.

# Například:
def is_member(val, aset):
    for el in aset:
        if el == val:
            return True
        if val < el:
            return False
        # print(el)
    return False


    
