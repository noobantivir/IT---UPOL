# ASCII tabulka - 7bitová
# ord("0") == 48
# ord("1") == 49
# ord("9") == 57
# chr(57) == 9
# ord("a") == 97
# chr(90) == Z

# ord_zero se používá ve Fcích, kde výsledek bude v 
def char_to_digit(char):
    ord_zero = ord("0")
    return ord(char) - ord_zero
"""
char_to_digit("2")
2
"""

def append_digit(number, digit):
    return (number * 10) + digit
"""
append_digit(12,4)
124
"""

# zadaný číslo ve formátu str převede int
def string_to_number(string):
    num = 0
    for char in string:
        digit = char_to_digit(char)
        num = append_digit(num, digit)
        print(char)
    return num

"""
string_to_number("123")
123
"""

# zadané číslo, převede do 16tkové soustavy
def digit_to_char(dig):
    ord_zero = ord("0")
    return chr(ord_zero + dig)

"""
digit_to_char(57)
'i'
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

"""
is_char_digit("a")
False
is_char_digit("0")
True
is_char_digit("22")
"""

def computer(operator, arg1, arg2):
    if operator == "+":
        return arg1 + arg2
    elif operator == "-":
        return arg1 - ar

# compute("+", 12, 5) => 17
# compute("-", 12, 5) => 7
 
def eval_expr(expr):
    result = 0
    operator = "+"
    arg_str = ""
    expr = expr + "+"
    for char in expr:
        if is_char_digit(char):
            arg_str = arg_str + char
        else:
            arg = int(arg_str)
            result = compute(operator, result, arg)
            arg_str = ""
            operator = char  
    return result

# eval_expr("10+3-2+12") => 23





















    



    
