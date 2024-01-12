ORD_ZERO = ord("0")


def char_to_digit(char):
    return ord(char) - ORD_ZERO

# char_to_digit("1") => 1

def append_digit(number, digit):
    return (number * 10) + digit


def string_to_number(string):
    num = 0
    for char in string:
        digit = char_to_digit(char)
        num = append_digit(num, digit)
        # print(repr(char), digit, num)
    return num

# string_to_number("123") => 123

# Převod řetězce,
# kde je číslo zapsané v šestnáctkové soustavě,
# na číslo. Cifry: 0-9, A, B, C, D, E, F
# "1F" => 16 + 15 = 31

def digit_to_char(digit):
    return chr(digit + ORD_ZERO)

# digit_to_char(9) => "9"

def get_last_digit(number):
    return number % 10

def remove_last_digit(number):
    return number // 10



def number_to_string(number):
    string = ""
    while number > 0:
        digit = get_last_digit(number)
        number = remove_last_digit(number)
        char = digit_to_char(digit)
        string = char + string
        print(number,
              digit,
              repr(char),
              repr(string))
    return string

# number_to_string(123) => "123"

# Zápis čísla v šestnáctkové soustavě.
# 31 => "1F"
#
# Možnost zadání soustavy.
# string_to_number("101", 2) => 5
# number_to_string(5, 2) => "101"
