"""
Read and write files
"""

path = 'c:\\Users\\fabio\\Documents\\Development\\Programming\\python\\language-python\\code\\test'

file = open(f'{path}\\text.txt')

print(file.read()) # Show all text.
# Hello World!
#    _____

file.seek(0) 

print(file.read())
# Hello World!
#    _____

file.seek(0)

print(file.readline())
# Hello World!

print(file.readline())
#     _____

print(file.readline())
# This is my new python course

print(file.closed)
# False

file.close()

print(file.closed)
# True