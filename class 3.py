# Type conversion and taking Input from user - dynamic programs

print(5+6)

name = input("Enter your name")
print("Welcome to the platform", name, "\nHow are you?")

first_name =  input("Enter your first name")
last_name = input("Enter your last name")
print("Full Name is ", first_name , " " ,last_name)


# dynamic programming and softwares require user input - e.g youtube
first_num = input("Enter the first number")
print(first_num)
print(type(first_num))
second_num = input("Enter the second number")
print(second_num)
print(type(first_num))

result = first_num + second_num
print(result)

result = int(first_num) + int(second_num)
print(result) # due to inputs in string - it will be concatenated


# convert from string to integer - typecasting

# user input is always in string - we need to typecase if needed as integer
# it is always in string as we can convert string into other datatypes but not vice versa

# to know the type of a variable
# type
type(4)
type(4.6)
type(6+5i)
type([1,2,3,4])

type(first_num)

# Kolkata can't be converted into integer - not possible 
# so type conversion must be possible before doing that

#there are 2 types of conversion-

# implicit - 4+5.5 = 9.5 - Python is intelligent enought to automatically convert it as  required - 
# implicit conversion
print(5+4j)
print(5+4j+9)

type('45')

# explicit - here we need to tell Python ecplicitly to convert the type sa shown below

# int
int('45') # given 45 as string - converting it into int
type(int('45'))


float(4)

str(5)

# True = 1 and False = 0 
bool(1)
bool(0)

complex(4)

list('Hello')

int('5')
int('Kolkata') # not possible - kolkata can't be stored as integer
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-26-e161ee1cd3bb> in <module>
----> 1 int('Kolkata')


a = 4.5
int(a)  # converting a to int - but it's a temporary operation

print(a) # now if we print a again - it'll be in it's original form - float
print(type(a)) # we can confirm the current datatype of a as well

# Type conversion is not permanent operation

print(a)

# if we
first_num = int(input("Enter the first number"))
second_num = int(input("Enter the second number"))

result = first_num + second_num
print(result)

# by default Python takes input as string, whether we give integer, decimal or any other.