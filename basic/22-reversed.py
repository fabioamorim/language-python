"""
Reversed
"""

tupla = tuple(range(10))

print(tupla)
# (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

tupla = reversed(tupla)

tupla = tuple(tupla)

print(tupla)
# (9, 8, 7, 6, 5, 4, 3, 2, 1, 0)