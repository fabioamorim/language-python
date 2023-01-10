"""
Loop:

for -> for item in interable:
            #execute

    iterable:
    - Strings
    - list [1,2,3,4,5]
    - range =range(1,10) - 1,2,3,4,5,6,7,8,9

"""

name = "Fabio"
lista = [1,2,3,4,5]
numbers = range(10,20)

for element in name:
    print(element)

for element in lista:
    print(element)

for element in numbers:
    print(element)

# enummerate:
for key, element in enumerate(name):
    print(f"Element: {element} key: {key}")
'''
Element: F key: 0
Element: a key: 1
Element: b key: 2
Element: i key: 3
Element: o key: 4
'''

for element in enumerate(name):
    print(f"{element}")
'''
(0, 'F')
(1, 'a')
(2, 'b')
(3, 'i')
(4, 'o')
'''

for _, element in enumerate(name):
    print(f"{element}", end='')
'''
Fabio
'''

print('\n')

qtd = 5

for n in range(1, qtd+1):
    print(n)