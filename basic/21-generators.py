"""
Generators

"""

lista = list(range(10))

result = (x for x in lista)
print(result)
# <generator object <genexpr> at 0x000001D85BD819C8>

result = list(result)

print(result)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

