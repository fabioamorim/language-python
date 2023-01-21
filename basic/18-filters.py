"""
Filter
"""

lista = list(range(20))
avarage = sum(lista) / len(lista)

print(lista)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

print(f'Avarage: {avarage}')
# Avarage: 9.5

result = filter(lambda x: x>avarage, lista)

result = list(result)

print(result)
# [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

data_collected = [None, 22, 55, None, 3.4, None, 100, None, None, 1, 2, 55, '']

print(data_collected)
# [None, 22, 55, None, 3.4, None, 100, None, None, 1, 2, 55, '']

data_collected = filter(None, data_collected)
data_collected = list(data_collected)

print(data_collected)
# [22, 55, 3.4, 100, 1, 2, 55]




