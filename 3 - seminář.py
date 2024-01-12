#Fce "while"
##number = 0
##number < 5
##True
##while number < 5:
##    print(number)
##    number = number + 1
"""vytiskne se nám čísla ve sloupci za sebou od 0-4.
5 se nevytiskne ALE!! Uloží se do mezipaměti a hodnota NUMBER = 5"""


#napiš Fci add, která sečte 2 čísla (4, 4) => 8
"""definujem si Fci add o 2 proměnných.
Fce while not = nám tady bude vyhodnocovat zda se y nerovná 0.
Pokud ne, bude se program opakovat"""
def add(x, y):
    while not (y == 0):
        y = y - 1
        x = x + 1
        print(x, y)
    return x
"""print(x, y) nám bude po každém cyklu tisknout hodnoty po zadání Fce"""


#Fce sub, která odečte 2 čísla (5, 3) = 2
def sub(x, y):
    while not (y1 == 0):
        y = y - 1
        x = x - 1
        print(x, y)
    return x

#Fce mult, která vynásobí 2 čísla (2, 2) = 4
def mult(x, y):
    z = 0
    while x != 0:
        x = x - 1
        z = add(z, y)
        print(x, y, z)
    return z

#Fce na porovnání čísel - menší nebo rovno
def lesq(x, y):
    while x != 0 and y != 0:
        x = x - 1
        y = y - 1
    return x == 0


#tam, kde to jde, použijte příkaz for.
#sum_up_to(5) = 1 + 2 + 3 + 4 + 5 = 10
def sum_up_to(x):
    r = 0
    for (i) in range(x): #pro "i" v rozsahu do X
        r = r + i
        print(i, r)
    return r



#sum_squares_up_to(3) => (0 * 0) + (1 * 1) + (2 * 2) + (3 * 3)
def sum_squares_up_to(x):
    r = 0
    for i in range(x):
        r = (i * i) + r
        print(i, r)
    return(r)


#1.1 odečtěte 2 čísla jen pomocí přičítání a odečítání jedničky
#a - b, kde b<=a
def plus_minus_one(a, b):
    while not b == 0 and not b > a:
        b = b - 1
        a = a - 1
        print(a, b)
    return False


#1.2
def print_backwards(x):
    while not x == 0:
        number1 = x % 10
        x = (x - number1) // 10
        print(number1)
        
        
#1.3 spočítá ciferný součet čísla

def add_digits(x):
    number2 = 0
    while not x == 0:
        number1 = x % 10
        x = (x - number1) // 10
        number2 = number1 + number2
    return number2

#1.4 nechápu zadání??
"""def is_number_square(x):"""

#1.5 ??

#1.6 ?

#1.7
def multi_add(a, b):
    result = 0
    while not b == 0:
        result = result + a
        b = b - 1
        print(a, b)
    return result


def another_multi(a, b):
    result = 0
    for repeats in range(b):
        result = result + a
        print(a, result)
    return result
1.10
def fact_number(x):
    result = x
    for i in range(1, x):
        x = x - 1
        result = result * x
        print(result, x)
    return result

"""zápočťák 2"""
def multi_add(x):
    result = 1
    for i in range(1,x):
        x = x - 1
        result = result * x
        print(i, result, x)
    return result















    

