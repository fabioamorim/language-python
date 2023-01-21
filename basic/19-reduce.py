"""
Reduce
"""

import functools

lista = list(range(10))

result = functools.reduce(lambda x, y: x+y, lista)

print(result)
# 45

result2 = 0

# the same result using loop
for number in lista:
    result2 += number

print(result2)
# 45