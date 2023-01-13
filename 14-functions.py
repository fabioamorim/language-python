"""
Functions:
"""

def simple_func():
    pass 

def func_without_param():
    print("This function doen's have paramenter")

def func_with_return():
    return 100

def func_with_param(name):
    """This function print a welcome greeting"""
    print(f'Welcome {name}')

func_without_param()
# This function doen's have paramenter

message = func_with_return()

print(message)
# 100

func_with_param('Fabio')
# Welcome Fabio

def pprint(param=''):
    print(param)

pprint("Hello World")
# Wello World
pprint()
#  

# *args

def func_sum(*args):
    # args is a tuple
    return sum(args)

result = func_sum(2,2,2,2)
print(result)
# 8

result = func_sum(10,100,90,89,78,45)
print(result)
# 412

numbers = [1,2,3,4,5]

print(func_sum(*numbers)) # the * will unpackage the list 
# 15


# **kwargs

def func_person(**kwargs):
    
    print(kwargs)

person = {'name': 'fabio',
            'age': 34
        }

func_person(name='fabio', age=34)
func_person(**person)
