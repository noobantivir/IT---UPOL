# ASCII tabulka - 7bitová
# ord("0") == 48
# ord("1") == 49
# ord("9") == 57
# chr(57) == 9

def char_to_digit(char):
    ord_zero = ord("0")
    return ord(char) - ord_zero
"""
char_to_digit("2")
2
"""


def append_digit(number, digit):
    return (number * 10) + digit


def string_to_number(string):
    num = 0
    for char in string:
        digit = char_to_digit(char)
        num = append_digit(num, digit)
    return num
"""
string_to_number("123")
123
"""


def digit_to_char(dig):
    ord_zero = ord("0")
    return chr(dig + ord_zero)
"""
digit_to_char(57)
'i'
digit_to_char(55)
'g'
digit_to_char(58)
'j'
digit_to_char(58)
'j'
digit_to_char(5)
'5'
digit_to_char(9)
'9'
"""

def number_to_string(num):
    string = ""
    while num != 0:
        last_digit = num % 10
        string = digit_to_char(last_digit) + string
        num = num // 10
    return string

""" number_to_string(123) == '123' """
        #string = string + digit_to_char(last_digit)
""" number_to_string(123) == '321' """


def is_char_digit(char):
    return ord("0") <= ord(char) <= ord("9")

def computer(operator, arg1, arg2):
    if operator == "+":
        pass
    
def eval_expr(expr):
    result = 0
    operator = "+"
    arg_str = ""
    for char in expr:
        if is_char_digit(char):
            arg_str = arg_str + char
        else:
            arg = int(arg_str)
            result = computer(operator, result, arg)
            arg_str = ""
            operator = char
        return arg

    























    



    
