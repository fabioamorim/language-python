"""
    Datatypes 

    - int <class 'int'>
    - float <class 'float'>
    - string <class 'str'> 
    - bool <class 'bool'> 

"""

age = 34
height = 1.75
name = 'Fabio'
enable = True

print(type(age)) # <class 'int'>
print(type(height)) # <class 'float'>
print(type(name)) # <class 'str'> 
print(type(enable)) # <class 'bool'> 

# Integer, float

print(10 + age) # 44
print(10 - age) # -24
print(10 * age) # 340
print(5/2) # 2.5
print(5//2) # 2 (int(5/2))
print(4%2) # 0
print(2**2) # 4 (2^2)
print(1_000_000_000) # 1000000000

heigth_t = int(height) # cast from float to integer

print(heigth_t) # 1

# bool
# True or False

if(enable):
    print('Is enable')
else:
    print('Is disable')

# not
print(not enable) # False

# or operation
# True or True - True
# Falser or True - True
# True or False - True
# False or False - False

print(True or enable) # True

# and operation
# True and True - True
# True and False - False
# False and True - False
# False and False - False

print(False and False) # False

# String

text1 = 'Is a string'
text2 = "Is other string"
text3 = """Strinng"""
text4 = '200'

print(text1)
print(text2)
print(text3)
print(text4)

store = "Joe's Store"

print(store)
print(store.upper()) # JOE'S STORE
print(store.lower()) # joe's store
print(store.title()) # Joe'S Store
print(store.split()) # ["Joe's", 'Store'] - Create a list 

#String slice

print(store[0]) # J
print(store[0:4]) # Joe'
print(store[::-1]) # erotS s'eoJ

# Replace
print(store.replace('J', 'R')) # Roe's Store

