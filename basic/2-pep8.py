"""
    PEP8 - Ptyhone Enhancement Proposal 

1 - User Camel Case to class's names.

class HttpRequest:
    pass 

class Peson:

    pass

2 - User lower case in function's name and variables

def sum():
    pass

def complex_sum():
    pass

number = 4

odd_number = 5

3 - Use 4 spaces for identation! If its not, we will have IndentationError.

if 'a' in 'banana':
    print('item')

4 - Blank lines

class User:
    pass
# blank line
# bliank line

5- Imports should be ever in separete lines.

import sys
import os

from types import StringType, ListType

from types import (
    StringType,
    ListType,
    SetType
    OtherType,
)

* Imports should be declare in the file head.

6 - Spaces in functions

Don't do:

func( do[ 1 ], { other : 2 } )

number         = 1
number_comples = 3.14

Do:

func(do[1], {other: 2})

number = 1
number_comples = 3.14

"""

