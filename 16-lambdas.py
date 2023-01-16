"""
Lambdas

"""

def func(x):
    return 3 * x + 1

print(func(3))
# 10

calc = lambda x: 3 * x + 1

print(calc(3))
# 10

person = lambda name, age: print(f"User: {name}, age {age}")

person('Fabio', 34)
# User: Fabio, age 34

numbers = list(range(1,11))

test = lambda *args: [print(number, end=' ') for number in args]

test(*numbers)
# 1 2 3 4 5 6 7 8 9 10
