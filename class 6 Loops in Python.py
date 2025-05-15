# Loops in Python - when repeatable tasks are done
# to iterate - 
# There are 2 types of loops in Python - while loop and for loop


number = int(input("Enter the number"))
i = 1
while (i<11):
    print(number,"*",i,"=",number * i)
    i+=1 # i = i+1


# For loop - iterates over range function or sequence

# range function - let's first understand it
list(range(1,11))
tuple(range(20,30))

list(range(51, 100))

list(range(51))  # this is same as list(range(0,51))

list(range(1,11,3))  #range function has 3 parameters start, stop, step
list(range(1,21,2))

list(range(10,1,-1))
list(range(10,-10,-2))



# Sequence - ordered elements _ now let's understand sequence

# String
"Kolkata"
'Kolkata'
["Kolkata","Delhi","Mumbai"]
['Kolkata', 'Delhi', 'Mumbai']
("Kolkata","Delhi","Mumbai")
('Kolkata', 'Delhi', 'Mumbai')

# for in in (10,9,8,7,6,5,4,3,2,1)

list(range(10,-5,-1))

for i in range(10,-5,-1):
    print(i)
print("Loop ended")

# for loops with strings
for i in "Ohio":
    print(i)

# for loops with list
for i in [1,2,3,5]:
    print(i)

# for loops with tuple
for i in (1,2,3,5):
    print(i)

# for loops with sets
for i in {1,2,3,5}:
    print(i)


# Implementation of for loop
# pattern printing using for loop:
'''
*
**
***
****
*****
'''

# Nested loop - slow solution as Time complexity is n square -
#  but there are few problem statements where we are bound to use nested loop

rows = int(input("Enter the number of rows"))

for i in range(1,rows + 1):
    for j in range(0,i):
        print("*",end=" ")
    print("")


# when u already know no of iterations to be made - then use for loop
# when we don't know number of iterations to be made then we use while loop - terminated by a given condition



# Write a program in Python to print all odd number between 1 and 50
for i in range(1,51):
    if (i%2 != 0):
        print(i, "is an odd number")


