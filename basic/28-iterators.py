"""
Iterators
"""

numbers = list(range(11))

iter1 = iter(numbers)

print(next(iter1))
# 0
print(next(iter1))
# 1
print(next(iter1))
# 2

for number in numbers:
    print(number, end=' ')
# 0 1 2 3 4 5 6 7 8 9 10 