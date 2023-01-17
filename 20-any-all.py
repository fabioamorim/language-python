"""
Any and All

"""

# All

lista = list(range(10))

print(lista)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(all(lista))
# False

lista = map(lambda x: x+1, lista)

lista = list(lista)

print(lista)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(all(lista))
# True

lista = []

print(all(lista))

# Any

print(any(lista))
# False

lista =list(range(10))

print(any(lista))
# True