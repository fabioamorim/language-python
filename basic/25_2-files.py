"""
Write in files
"""

path = 'c:\\Users\\fabio\\Documents\\Development\\Programming\\python\\language-python\\code\\test'

with open(f'{path}\\new.txt', 'w') as file:
    file.write('This is a new row\n')
    file.write('This is the last row')