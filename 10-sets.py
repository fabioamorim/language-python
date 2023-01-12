"""
Sets

"""

print(type({1,}))
# <class 'set'>

n1 = {1,2,3,4,5,5,4}

print(n1)
# {1, 2, 3, 4, 5}
print(type(n1))
# <class 'set'>

lista = [1,2,3,3,3,4,4,5]

n1 = set(lista)

print(n1)
# {1, 2, 3, 4, 5}

# add new element in set
n1.add(100)
print(n1)
# {1, 2, 3, 4, 5, 100}

# remove item
n1.discard(2)
print(n1)
# {1, 3, 4, 5, 100}

n1.remove(100)
print(n1)
# {1, 3, 4, 5}

n1.pop() # remove the first element
print(n1)
# {3, 4, 5}

# remove all elements
n1.clear()
print(n1)
# set()

n1 = set(range(11))
# {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

n2 = set(range(8,20))
# {8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19}

# difference between two sets

print(n1.difference(n2))
# {0, 1, 2, 3, 4, 5, 6, 7} - these elements are in n1 but are not in n2

n3 = n1.difference(n2)

print(n3)
# {0, 1, 2, 3, 4, 5, 6, 7}

print(n1)
# {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

n1.difference_update(n2)

print(n1)
# {0, 1, 2, 3, 4, 5, 6, 7}


n1 = set(range(11))
# {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

n2 = set(range(8,20))
# {8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19}

## intersection
n3 = n1.intersection(n2)
print(n1, n2, n3)
# {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10} {8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19} {8, 9, 10} <- 8, 9, 10 are in n1 and n2

n1.intersection_update(n2) # removes the items in n1 that are not present in n2.
print(n1)
# {8, 9, 10}

print(n1.issubset(n2)) # return true if n1 is n2 subset
# True

print(n1.isdisjoint(n2)) # return true if none of the items are presnt in both sets. n1 {8, 9, 10}, n2 {8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19}
# False

print(n2.issuperset(n1)) # return true if all n1 items are in n2
# True

# symmetric_difference

n1 = {100, 1, 99, 8, 66, 0}
n2 = {1 , 2, 100, 8,0, 90}

print(n1.symmetric_difference(n2))
# {2, 66, 99, 90} -  return a set with the symmetric differences of two sets.

n1.symmetric_difference_update(n2)
print(n1)
# {66, 99, 2, 90} - n1 recive the new set 

n1 = set(range(11))
# {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

n2 = set(range(8,20))
# {8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19}

#union
n3 = n1.union(n2)
print(n3)
# {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19} - create a new set with all elements

n1.update(n2)
print(n1)
# {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19} - update n1 set with n2 elements