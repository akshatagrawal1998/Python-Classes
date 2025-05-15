# Keywords and Variables in Python:
# print is different with Print
"""
Keywords
Python is a case sensitive programming language - difference between upper and lower case
In programming, a keyword is a word that is reserved by a program because the word has a special meaning. 
Keywords can be commands or parameters. Every programming language has a set of keywords that cannot be used as variable names
"""

# High level prog - we write in Eng lang - simple e.g for, if, etc
# compiler or interpreter converts high level code into low level code
# compiler has set meanings for some keywords - which are used for conversion
# compiler may get confused if we use keyword in programming -


# python has 33 keywords
import keyword
print(keyword.kwlist)
# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 
# 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 
# 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 
# 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

'''
Identifiers
A Python identifier is a name used to identify a variable, function, class, module or other object.

Rules for setting Identifiers:

- can only start with an alphabet or underscore (_)
- Followed by 0 or more letter,_ and digits
- keywords cannot be used as an identifiers
'''


a=3
print(a)
type(a)


# valid name of variables
name = "Akshat"
a = 2
_ = 'xyz'
name_first = "Stephen"
_firstname = "King"
Name = "A"
NAME = "Adsjad"

# below part will show an error
# invalid 
# 1 = "abc"
# first-name = "boss"
# False = "Nitish"
print(False)


# variables in Python

# Python automatically detects datatype of a variable - dynamic typing  e.g PHP, Python
# Static typing - where we need to specify the datatype of the variable - e.g C language

name = "Michael" # no need to tell explicitly that it is a string
x=5 
type(x)
y = 5.6

# value of variables can be over written
name = 'Nitish'
print(name)
# it'll produce output as Nitish

name = 'Hello world'
print(name)
# it'll produce output as Hello world

# no variable declaration
print(name)

# value of variables can be over written with any datatype value - this is called dynamic binding
# static binding - eg in C lang - int a = 5, now we can't update the value of a with any other data type value


a = 3
type(a)

a='Akshat'
type(a)

name = 4
print(name)
# it'll produce output as 4

name = True # boolean
print(name)
# it'll produce output as True

# special syntax
a = 5; b=6; c=7  # declare multiple variable in single line
print(a)
print(b)
print(c)

a,b,c = 4,5,6    # declare multiple variable in single line
print(a)
print(b)
print(c)


a = b =c =6    # declare multiple variable in single line with same value
print(a)
print(b)
print(c)