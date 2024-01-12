"""
>>> int("1243")
1243
>>> str(1243)
'1243'
"""

def is_char_digit(char):
    return ord("0") <= ord(char) <= ord("9")

"""
>>> is_char_digit("a")
False
>>> is_char_digit("6") 
True
"""
def compute(operator, arg1, arg2):
    if operator == "+":
        return arg1 + arg2
    elif operator == "-":
        return arg1 - arg2
    
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
        print(repr(char),
              is_char_digit(char),
              repr(operator),
              repr(arg_str),
              result)
    return result

# eval_expr("10+3-2+12") => 23

# Vytvořit kalkulačku.
"""
>>> input("Zadejte výraz: ")
Zadejte výraz: 12+34
'12+34'
"""

# Postfixová kalkulačka
#
# eval_postfix_expr("1 2 +") => 3
# eval_postfix_pexpr("1 2 3 + +") => 6
# eval_postfix_pexpr("12 2 -") => 10
#
# Udržujeme si pole hodnot:
# []  "1 2 3 + +"
# [1] "2 3 + +"
# [1, 2] "3 + +"
# [1, 2, 3] "+ +"
# [1, 5] "+"
# [6] ""
#
# 1. Čísla přidáváme nakonec pole.
# 2. Operátor nahradí poslední dva prvky pole
#    výsledkem příslušné operace.
