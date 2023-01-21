"""
Nested lists

"""

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
]

print(matrix)
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(matrix[0])
# [1, 2, 3]
print(matrix[1])
# [4, 5, 6]
print(matrix[2])
# [7, 8, 9]

# show the elements 
for row in matrix:
    for number in row:
        print(number, end=' ')
# 1 2 3 4 5 6 7 8 9 

# Atention!
# For comprehensions example, check 15-comprehesions.py file
# the same loop result with comprehension list.

[[print(number, end=' ') for number in row] for row in matrix]
# 1 2 3 4 5 6 7 8 9