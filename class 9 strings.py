'''Strings are sequence of Characters

In Python specifically, strings are a sequence of Unicode Characters

Creating Strings
Accessing Strings
Adding Chars to Strings
Editing Strings
Deleting Strings
Operations on Strings
String Functions
'''

# Creating
c = 'Hello'
print(c)
type(c)
c = "Hello. it's raining outside"
print(c)

str = """Adam is my teacher.
        He is good in teaching. 
                I give him 5* """
type(str)


c = '''Hello'''
print(c)

# multi line strings
c = """Hello"""
print(c)

c = str("Hello")
c


# Accessing Substrings from a String
# Concept of Indexing
c = "hello"
print(c)

print(c[0])
print(c[1])
print(len(c))


string = ['Adam', 'Mike', 'Julie', 'Michael']
string[-3]
string[-5]


# Types of Indexing
# Postive Indexing
# Negative Indexing

#Indexing lets us extract a single character from a string
print(c)  # Hello
print(c[3])
print(c[-3])
print(c[-1])
print(c[-2])



# Slicing - to extract multiple characters at once from a string
c = "Hello World"
print(c)
# range(0,4)
print(c[0:5]) # from 0 to 4
print(c[3:7]) # lo W
print(c[2:9])  # llo Wor
print(c[2:]) # from 2 to end  [start:stop]

print(c[:4]) # from 0 to 3

print(c[:]) # all

print(c)

# range(start:stop:step)
# c = "Hello World"
print(c[0:8:2]) #giving step size also - from 0 to 7 on a step of 2 
print(c[0:8:3]) # HlW
print(c[0::3]) # HlWl

print(c[0:6:-1]) # empty string as -ve step can't be used while using +ve indexes
print(c)
print(c[-5:-1:2]) #

s = "Mike"  # ekiM
print(c[::-1]) # reverse a string -

print(c[-1:-5:-1]) # from -1 to -4 and reversed




# i or  l[i]

l=[1,2,4,564,21,2,321214,342,123,24,3534,657,56,8567,3,21]
for i in (range(1,10)):  # 1,2,3,4,5,6,7,8,9
    print(l[i])

for i in range(1,10):
    print(i)



# Editing and Deleting in String
c = "Hello"
print(c)
# String are immutable
c[0] = 'X' # trying to update the char at 0 from H to X - 

# TypeError: 'str' object does not support item assignment
# Strings are a Immutable Data Type

# we can re assign but can't edit
c = "world"
print(c)


c[5] = "X" # error - can't add or edit characters


# Deletion
print(c)
del c # del is the keyword to delete astring
print(c) # error as c is now deleted

c = "hello"
print(c)

del c[0] # error as string is immuatable


'''
Operations on Strings
Arithmetic Operations
Relational Operations
Logical Operations
Loops on Strings
Membership Operations
'''

# no mathematical operator other than + and * works with strings


# string1 + str2

print("Hello" + "-" + "world")  # concat string

# by default any input is taken as string in python
a = input("enter a number")
b = input("enter another number")
print(a+b)  # so when we do arithmetic addition on strings, it will concatenate them.

print(int(a) + int(b))

print("*"*50) # string multiplication

print("Hello "*4)

# Comparision opeartors
print("Hello" == "World")

"Hello" != "WOrld"

print("Mumbai" > "Pune")
# Lexiographically - the word which comes first in Oxford dictionary is treated smaller

"Goa" < "Kolkata"

"kol" < "Kol" # small letters come after capital letters

# Logical operators
# empty string is treated as False and non empty string as True


"hello" and "world" # logical and 

"" and "Hello"

"" or "world"

"hello" or "world"

"hello" and "world"

print(not "hello")

not ""


c = "hello world"
print(c[::-1])

for i in c[::-1]:
    print(i)


# Membership operators

c = 'hello world'
'h' in c

'H' in c

'world' not in c



"""
Common Functions used with strings
len
max
min
sorted
"""

c = "kolkata"
len(c)

ord('k')
ord('o')
ord('l')
ord('a')
ord('t')

max(c) # based on ASCII characters

min(c)

sorted(c,reverse=True) # descending order based on ASCII characters


# functions only applicable on string datatype - not on any other
# adam -> ADAM -> Adam
# 1. Capitalize/Title/Upper/Lower/Swapcase
"it is raining today".capitalize() # first letter capital

# It Is Raining Today
"it is raining today".title() # capitalize first letter of every word
c = "kolkata"

c.upper().lower()
"KoLkAtA".swapcase()
 
#2. Count
"it is raining".count("x")
"it is raining".count("i")
"it is raining".count("is")
 
#3. Find vs Index
"it is raining".find("x") # first occurence of the character 
# -1 as output means the given char is not present in the string when we use find func.
# when it is not present - index funtion returns error
# so it's better to use find to atleast avoid error

"it is raining".index("x")

 
# 4. endswith/startswith
"it is raining".endswith("ingef")

"it is raining".startswith("it")

#5. format string 
"Hello my name is {} and I am {}".format("Adam",30)
# {} is replaced with the given character

# we can also provide the order - 
"Hello my name is {1} and I am {0}".format("Nitish",30)

"Hello my name is {age} and I am {name}".format(name = "Nitish",age = 30)

"Hello my name is {name} and I am {name}".format(name = "Nitish",age = 30, weight = 70)

#6. isalnum/ isalpha/ isdecimal/ isdigit/ isidentifier

"FLAT20".isalnum()  # alphanumeric - either all alphabets or numeric

"FLAT20&".isalnum()

"FLAT20".isalpha()

"20".isdigit()

"20A".isdigit()

"hello_world".isidentifier()

"hello".is


#7. Split - useful in NLP - convert texts into tags

"who is the pm of india".split() # when nothing is passes it is split as per space
#return a list

# we can split acc to anything - like below split by pm - 
# so it will break into 2 strings - 1 before pm and other after it and returns a list
"who is the pm of india".split("pm")
#
"who is the pm of india".split("x")



#8. Join
" ".join(['who', 'is', 'the', 'pm', 'of', 'india']) # joining using space

"-".join(['who', 'is', 'the', 'pm', 'of', 'india'])  # # joining using dash(-)



# 9. Replace

"Hi my name is Nitish".replace("Nitish","Amit")

 
#10. Strip - remove trailing and leading space

name = "               nitish              "
print(name)
# now when we use strip function
name.strip()

# Explore more string functions on official doc or Google