"""
Collections: Counter

"""

from collections import Counter

lista = list(range(100,120))

result = Counter(lista)

print(type(result))
# <class 'collections.Counter'>

print(result)
# Counter({100: 1, 101: 1, 102: 1, 103: 1, 104: 1, 105: 1, 106: 1, 107: 1, 108: 1, 109: 1, 110: 1, 111: 1, 112: 1, 113: 1, 114: 1, 115: 1, 116: 1, 117: 1, 118: 1, 119: 1})
# for element 100 it found 1 item

print(Counter('Fabio Batista do Amorim'))
# Counter({'a': 3, 'i': 3, 'o': 3, ' ': 3, 't': 2, 'm': 2, 'F': 1, 'b': 1, 'B': 1, 's': 1, 'd': 1, 'A': 1, 'r': 1})

lorem_ipsum = """ Lorem Ipsum is simply dummy text of the printing and typesetting industry.
            Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
            when an unknown printer took a galley of type and scrambled it to make a type specimen book.
            It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.
            It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages,
            and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."""

print(Counter(lorem_ipsum))
"""
Counter({' ': 146, 'e': 59, 't': 43, 's': 39, 'n': 38, 'i': 32, 'a': 28, 'o': 25, 'r': 24,
             'm': 18, 'p': 18, 'u': 17, 'l': 17, 'd': 16, 'h': 14, 'y': 13, 'g': 11, 'c': 10,
             'k': 7, 'I': 6, 'f': 6, 'w': 6, 'L': 5, '\n': 5, 'b': 5, 'v': 5, '.': 4, ',': 4,
              '0': 3, 'x': 2, '1': 2, "'": 1, '5': 1, '9': 1, '6': 1, 'A': 1, 'P': 1, 'M': 1})
"""