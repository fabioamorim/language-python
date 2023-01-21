"""
    For recive user data in terminal, we can user input() function.

    variable = input()

"""

name = input("What's you name?\n")
age = int(input("How old are you?\n"))

print("Name: %s is %s years old" %(name, age))
print("Name: {0} is {1} years old".format(name, age))
print(f"Name: {name} is {age} years old")