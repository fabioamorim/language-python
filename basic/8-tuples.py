"""
Tuples: Tuples are immutables!

(1,2,3,4,5)

"""
print(type(()))
#<class 'tuple'>

t = (1,2,3,4)

print(type(t))
# <class 'tuple'>

t2 = 1,2,3

print(type(t2))
# <class 'tuple'>

t3 = (4,)

print(type(t3))
# <class 'tuple'>

t4 = tuple(range(11))

print(t4)
# (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# count how many time the number is in array
print(t.count(2))
# 1

# tuple unpackaged
n1, n2, n3 = t2

print(n1, n2, n3)
# 1 2 3

print(sum(t))
# 10
print(max(t))
# 4
print(min(t))
# 1
print(len(t))
# 4

# tuple concatenation 

t = t2 + t3 

print(t)
# (1, 2, 3, 4)

# show elements

for number in t:
    print(number)
'''
1
2
3
4
'''

for index, number in enumerate(t):
    print(f'Value: {number} - index: {index}')

'''
Value: 1 - index: 0
Value: 2 - index: 1
Value: 3 - index: 2
Value: 4 - index: 3
'''

month = ('january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december')

print(month)
# ('january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december')

print(month[4])
# may

