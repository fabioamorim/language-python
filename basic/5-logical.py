"""
if/else/elif

and/or/not/is

and 

True and True - True
True and False - False
False and True - False
False and False - False

or 

True or True - True
True or False - True
False or True - True
False or False - False

"""

number = 100

if number < 100:
    print("less than 100")
else:
    print("equal or more than 100")

number > 500

if number < 500:
    print("less than 500")
elif number > 500:
    print("more than 500")
else:
    print("equal 500")

#--------------------------------------

enable = False 
logged = False 

if enable and logged:
    print("Welcome user")
else:
    print("The account is disable")

if not enable:
    print("The account is disable")

if not logged:
    print("The user is not logged")

print(enable is False) # Is enable False? True