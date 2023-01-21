"""
Common errors

- NameError
- ZeroDivisionError: number/0
- SyntaxError
- IndexError

"""

# printf("test")
# NameError: name 'printf' is not defined

# 1/0
# ZeroDivisionError: division by zero

# def funcao:
    #print('Hello World')
# SyntaxError: invalid syntax

# lista = list(range(10))

# print(lista[12])
# IndexError: list index out of range

"""
try:
    len(True)
except TypeError as err:
    print(f'The app generated error: {err}')
"""
#The app generated error: object of type 'bool' has no len()

"""
try:
    10/0
except NameError as err1:
    print(err1)
except ZeroDivisionError as err2:
    print(err2)
except SystemError as err3:
    print(err3)
"""
# division by zero

