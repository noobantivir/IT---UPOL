#def = zápis fce, get_square = název Fce

#funkce na výpočet obsahu čtverce
def get_square(number):
    return number **2
"""get_square(6)
36"""

#po zadání čísla nám program vypíše poslední číslici
# % je celočíselný zbytek PO dělení
def get_last_digit(a):
    return a % 10
"""get_last_digit(783937)
7"""

#po zadání čísla nám program "odstraní" poslední číslici čísla
def remove_last_digit(b):
    return (b // 10)
"""remove_last_digit(89216388)
8921638"""

#Fce append_digit(12, 4) = 124 složí zadaná čísla zasebou dohromady
def append_digit(number, digit):
    return (number * 10) + digit

#úkol: Fce vrátí předposlední cifru čísla 124 -> 2
def get_2nd_last_digit(xx):
    return (get_last_digit(remove_last_digit(xx)))
"""dosadí číslo v "XX" do Fce remove last digit, poté dosadí výsledek do
get last digit a tím vyhodnotí předposlední cifru čísla"""

def get_3rd_last_digit(xxx):
    return (get_last_digit(remove_last_digit(remove_last_digit(xxx))))
"""dosadí číslo v "XXX" do Fce remove, pak výsledek se zopakuje ve stejné Fci
a poté bude vyvolána poslední Fce get last digit"""

#Fce na sečtení 2 čtverců
def sum_squares(x, y):
    return get_square(x) + get_square(y)

#:make_number(1, 2, 5) => 125 program na složení čísla po zadáná číslic
def make_number(x1,x2,x3):
    return (append_digit(append_digit(x1, x2), x3))
"""po zadání 3 číslic, se první 2 číslice vloží do Fce pro složení číslic,
poté celou Fci zopakujem s nejprve již vytvořeným číslem a posledním zadaným"""

#1.9 úkol: napiš Fci, která prohodí cifry trojcif. čísla. 157-> 751
def swap_numbers(snumber):
    return make_number(get_last_digit(snumber),
                       get_2nd_last_digit(snumber),
                       get_3rd_last_digit(snumber))
"""swap_numbers(824)
428
"""

#Podmínky
#logické hodnoty (true a false)

#funkce na zjištění sudého čísla
def is_even(number):
    return (number % 2) == 0

#Fce na zjištění dělitolnosti 2 čísel
def is_nonzero_divisor(a1, a2):
    return (a1 % a2) == 0

#Fce na zjištění sudého čísla
def is_even2(number2):
    return (is_nonzero_divisor(number2, 2))

#2.3 pythagorova věta c*2= a*2 + b*2
def add_squares(a, b, c):
    return c**2 == a**2 + b**2

#2.5 predikát - zda je číslo kladné
def is_non_negative(x):
    if x <= 0:
        return False
    else:
        return True


#2.6 zda zadané číslo x patří do intervalu a-b

def number_from_range(x, a, b):
    if x <= b and x >= a:
        return True
    else:
        return False

#2.8 dělitel 2 nebo 3
def which_div(number):
    if number % 2 == 0 or number % 3 == 0:
        print (number % 2 == 0, number % 3 == 0)

#2.10 mají výrazy not (number1 == number2) a number1 != number2 vždy
#stejnou hodnotu? 
def porovnej(number1, number2):
    return not (number1 == number2)

def porovnej2 (number1, number2):
   return number1 != number2

#Predikát zda je číslo dělitelné 10
def div_ten(x):
    print (x % 10 == 0)

#napište Fci, která vrátí absolut. hodnotu čísla.
def absolute_value(abs_number):
    if abs_number >= 0:
        return abs_number
    else:
        return -abs_number
#3.1
def add_subtract_numbers(x1,x2):
    print(x1 + x2, x1 - x2)

#3.2
def add_square(x1, x2):
    return (get_square(x1) + get_square(x2))
#4.2
def is_devisor(x1, x2):
    if x1 % x2 == 0:
        print(x1)
    else:
        print(False)

#4.3

def zero_one_minus(x):
    if x > 0:
        return 1
    if x == 0:
        return 0
    else:
        return -1


    













        
