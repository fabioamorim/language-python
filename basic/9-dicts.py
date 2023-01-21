"""
Dictionaries:

person = {
            name : 'Fabio', 
            age: 31
        }

"""

print(type({}))
# <class 'dict'>

person = {
            'name' : 'Fabio', 
            'age': 34
        }

print(person)
# {'name': 'Fabio', 'age': 34}

person2 = dict(name='Mary', age=22)

print(person2)
# {'name': 'Mary', 'age': 22}

print(person['name'])
# Fabio
print(person['age'])
# 34

print(person.get('name'))
# Fabio
print(person.get('age'))
# 34

# remove all elements
person2.clear()
print(person2)
# {}

# copy dict
person3 = person.copy()

print(person3)
# {'name': 'Fabio', 'age': 34}

person3['name'] = 'Test'

print(person)
# {'name': 'Fabio', 'age': 34}
print(person3)
# {'name': 'Test', 'age': 34}

# try to found a property that doen'st exists, if not, return None
weight = person.get('weight', None)

print(weight)
# None

# check if the key exists 
print('name' in person)
# True


bill = {'jan':200, 'feb':300}
print(bill)
#{'jan': 200, 'feb': 300}

#add new key and value
bill['mar'] = 400

print(bill)
#{'jan': 200, 'feb': 300, 'mar': 400}

april = {'april': 600}

bill.update(april)

print(bill)
# {'jan': 200, 'feb': 300, 'mar': 400, 'april': 600}

# update data
bill['april'] = 1000
bill.update({'jan': 700})

print(bill)
# {'jan': 700, 'feb': 300, 'mar': 400, 'april': 1000}

# remove data
print(f"{bill.pop('april')} was removed")
# 1000 was removed

print(bill)
# {'jan': 700, 'feb': 300, 'mar': 400}

del bill['mar']
print(bill)
# {'jan': 700, 'feb': 300}

for key in bill:
    print(key)
"""
jan
feb
"""

for key in bill:
    print(f'{key} : {bill[key]}')
"""
jan : 700
feb : 300
"""

print(bill.keys())
# dict_keys(['jan', 'feb'])

for key in bill.keys():
    print(bill[key])
"""
700
300
"""

print(bill.values())
# dict_values([700, 300])

for value in bill.values():
    print(value)
"""
700
300
"""

for key, value in bill.items():
    print(f'key:{key} - value:{value}')