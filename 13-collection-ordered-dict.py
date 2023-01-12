from collections import OrderedDict

dict_1 = {'a':1, 'b':2, 'c':3, 'd':4, 'e': 5}

print(dict_1)
# {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

for key, value in dict_1.items():
    print(f'{key}:{value}')

'''
a:1
b:2
c:3
d:4
e:5
'''

print('\n')

dict_2 = OrderedDict({'a':1, 'b':2, 'c':3, 'd':4, 'e': 5})

for key, value in dict_2.items():
    print(f'{key}:{value}')
