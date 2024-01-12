def reverse(array1):
    result = []
    temp = len(array1)
    for i in range(len(array1)):
        temp = temp - 1
        result = result + [array1[temp]]
    return result

def rev(array):
    temp = []
    for el in array:
        temp = [el] + temp
    return temp

def rev2(array):
    temp = []
    for el in array:
        temp = temp + [el]
    return temp

def count_char(a):
    return len(a)

#spočítá nám počet zadaného písmena v textu
def count_char_in(char, b):
    result = 0
    for i in range(len(b)):
        if char == b[i]:
            result = result + 1
    return result

def count_char2(char, string):
    counter = 0
    for char1 in string:
        if char1 == char:
            counter = counter + 1
    return counter

# is_substring_from("ananas", nan, 1)
#správné řešení
def is_substring_from(string1, string2, index):
    index = 0
    if not len(string1) < len(string2) + index:
        return False
    for i in range(len(string2)):
        char1 = string1[i + index]
        char2 = string2[i]
        if char1 != char2:
            return False
    return True


#
def is_substring(string1, string2):
    for i in range(len(string1)):
        if is_substring_from(string1, string2, index):
            return True
    return False


#substring_count("aaaa", "aa") > 2
"""úkol"""


#replace_char("ananas", "a", "ga")
def replace_char(string1, string2, string3):
    result = ""
    index = 0
    while index < len(string1):
        if is_substring_from(string1, string2, index):
            result = result + string3
            index = index + len(string2)
        else:
            result = result + string1[index]
            index = index + 1
    return result




            
    
        
    







        
            
