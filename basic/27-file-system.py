import os 

print(os.getcwd())
# c:\Users\fabio\Documents\Development\Programming\python\language-python

os.chdir('..')

print(os.getcwd())
# c:\Users\fabio\Documents\Development\Programming\python

os.chdir('language-python')

print(os.getcwd())
# c:\Users\fabio\Documents\Development\Programming\python\language-python
