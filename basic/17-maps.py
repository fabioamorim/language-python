"""
Map

"""

values = [2,3,4,1.2,7.88,99]

def calc(x):
    return 3.14 * (x * x)

results = map(calc, values)

print(results)
# <map object at 0x0000021F11EB7E48>

lista = list(results)

print(lista)
# [12.56, 28.26, 50.24, 4.5216, 194.976416, 30775.14]

results = map(lambda x: 3.14 * (x * x), values)

lista = list(results)

print(lista)
# [12.56, 28.26, 50.24, 4.5216, 194.976416, 30775.14]
