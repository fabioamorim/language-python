"""
Comprehensions

- list comprehensions

[data for data in iterable]

"""

n1 = list(range(11))
print(n1)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# conversion form

n2 = list()

for number in n1:
    n2.append(number)

print(n2)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# comprehension
n3 = [x for x in n1]
print(n2)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

n4 = [number * 2 for number in n1]
print (n4)
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

def calculate(number):
    return number * 2 + 5

def number_to_sintrg(number):
    return str(number)

n5 = [calculate(number) for number in n1]
print(n5)
# [5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]

n6 = [number_to_sintrg(number) for number in n1]
print(n6)
# ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

# with condiction

print([number for number in n1 if number % 2 ==0])
# [0, 2, 4, 6, 8, 10]

print([number * 2 if number % 2 == 0 else number /2 for number in n1])
# [0, 0.5, 4, 1.5, 8, 2.5, 12, 3.5, 16, 4.5, 20]