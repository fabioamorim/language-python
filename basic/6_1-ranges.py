"""
Ranges

range(value)
"""

for i in range(10): # range(0,10)
    print(i, end='')
# 0123456789

for i in range(-1,10):
    print(i, end='')
# -10123456789

for i in range(1,10,2):
    print(i, end='')
# 13579

print("\n")
for i in range(10, 1, -1):
    print(i, end='')
# 1098765432

lista = list(range(10))

for i in lista:
    print(i, end='')
# 0123456789