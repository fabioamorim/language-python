"""
Lists

numbers = list(range(10))

"""
numbers = list(range(10))

print(numbers) 
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(type(numbers))
# <class 'list'>

numbers2 = [1,2,3,4,5]

print(numbers2)
# [1, 2, 3, 4, 5]

print(type(numbers2))
# <class 'list'>

print(type([]))
# <class 'list'>

print(numbers2[1])
# 2 

# show all elements
for number in numbers:
    print(number)
# 0123456789

# add new element
numbers.append(100)
print(numbers)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 100]

numbers.append(100)

# add new element by position .insert(position, value)
numbers.insert(1, 99)
print(numbers)

# add new list inside current list.
# The new list will be considered one element in the list!
numbers.append([101,102,103])
print(numbers)
#[0, 99, 1, 2, 3, 4, 5, 6, 7, 8, 9, 100, 100, [101, 102, 103]]

# add some eleements in the list
numbers.extend([200,203,204])
print(numbers)
[0, 99, 1, 2, 3, 4, 5, 6, 7, 8, 9, 100, 100, [101, 102, 103], 200, 203, 204]

n1 = list(range(1,5))
n2 = list(range(5,10))

# the same extend function.
n3 = n1 + n2
print(f'n3: {n3}')

# remove element by index
print(f'{numbers.pop(12)} was removed')
print(numbers)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 99, 100]

# remove element
numbers.remove(99)
print(numbers)

# remove all elements from the list
numbers2.clear()
print(numbers2)
# []

# count how many time the number is in array
print(numbers.count(100))
# 2

print(numbers.index(0))

# order the list
#numbers.sort()

print(numbers)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 99, 100, 100]

# copy list 
numbers2 = numbers.copy()

print(numbers)
print(numbers2)
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 100, [101, 102, 103], 200, 203, 204]
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 100, [101, 102, 103], 200, 203, 204]

numbers.pop()

print(numbers)
print(numbers2)
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 100, [101, 102, 103], 200, 203]
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 100, [101, 102, 103], 200, 203, 204]
