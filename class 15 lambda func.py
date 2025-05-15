# lambda Function in Python
'''
Properties:
one liner
anonymous function - they don't have any name
Syntax - lambda(keyword) x(input) : expression
'''



# a function to calc square of a number
def square(x):
    return x**2

square(9)

pow(9,2)
print(9**2)

# same using lambda function
y = lambda x : x**2
y(9)

# sum of 2 integers
a = lambda x,y : x+y
a(4,5)

# to check whether first letter of given string is a or not?
b = lambda x : x[0] == 'a'
b('apple')
b('banana')

b = lambda x :"even" if x%2==0 else "odd"
b(67)
b(76)


# Higher order function- func which needs another func as input
# we give input to it and also tell what to do - basically we control the behaviour of this function
# In normal functions, it basically does only 1 type of task
L = [11,12,14,12,21,42,65,876,35]
# find sum of all even numbers
# find sum of all odd numbers
# find sum of all numbers divisible by 3

def return_sum(func, L):
    result = 0
    for i in L:
        if func(i):
            result = result+i
    return result

x = lambda x : x%2 == 0
y = lambda x : x%2 != 0
z = lambda x : x%3 == 0
print(return_sum(x,L))
print(return_sum(y,L))
print(return_sum(z,L))

# Inbuilt HUF- map, reduce, filter

# e.g -
L = [1,2,3,4,5,6,7,8]
map(lambda x : x*3 , L) # returns a map object
list(map(lambda x : x*3 , L))

list(map(lambda x : x%2 == 0 , L))


# E.g - map()
# fetch student names from given list of dictionaries
students = [
{
    "name" : "Adam",
    "gender"  : "Male"
},
{
    "name"  :"Eve",
    "gender" : "Female"
}
]
list(map(lambda x : x['name'] , students))



# filter function: work acc to given condition
l = [1,2,3,4,6,7,8,9,6,4,32,432,42]
# find all numbers from list greater than 4
list(filter(lambda x : x>4 , l))

fruits = ['apple', 'orange', 'mango', 'guava']
# find fruits whose name contain "e"
list(filter(lambda x : "e" in x , fruits))


"""
# Quick exercise: 
Write a lambda function that takes a list of strings as input and returns a list of strings with their first letter capitalized.

capitalize_first_letter = lambda strings: list(map(lambda s: s.capitalize(), strings))

# Test the lambda function
words = ["apple", "banana", "cherry", "date"]
result = capitalize_first_letter(words)
print(result)  # Output: ['Apple', 'Banana', 'Cherry', 'Date']

"""

capitalize_first_letter = lambda strings: list(map(lambda s: s.capitalize(), strings))


words = ["apple", "banana", "cherry", "date"]
list(map(lambda s: s.capitalize(), words))
# Test the lambda function
result = capitalize_first_letter(words)
print(result)  # Output: ['Apple', 'Banana', 'Cherry', 'Date']


fruits = ['Orange', 'Apple', 'Guava', 'Mango']
[fruit for fruit in fruits if fruit[0] == 'O']