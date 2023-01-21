from collections import defaultdict

dict_1 = defaultdict(lambda: None)

print(dict_1)
# defaultdict(<function <lambda> at 0x0000023A9A9CB438>, {})

dict_1['name'] = 'Jhon'

print(dict_1)
# defaultdict(<function <lambda> at 0x000001CD32A1B438>, {'name': 'Jhon'})

print(dict_1['age'])

print(dict_1)
# defaultdict(<function <lambda> at 0x0000025C463AB438>, {'name': 'Jhon', 'age': None})