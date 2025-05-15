# Literals and Operators in Python

''' Literals
Literal is a raw data given in a variable. In Python, there are various types of literals they are as follows:

Numeric Literals
String Literals
Boolean Literals
Special Literals
'''

# 1. Numeric Literals

a = 0b1010 #Binary Literals - stored as binary but printed as decimal only
print(a)
b = 100 #Decimal Literal 
c = 0o310 #Octal Literal
d = 0x12c #Hexadecimal Literal
print(a, b, c, d)


#Float Literal
float_1 = 10.5 
float_2 = 1.5e2 # very large numbers
float_3 = 1.5e-3 # very small number
print(float_1, float_2,float_3)



#Complex Literal 
x = 3.14j # can only have real or only imaginary part
print(x, x.imag, x.real)


# 2. String Literals
# manily there are 3 ways to initialize string literals in Python

string = 'This is Python' # single quotes
strings = "This is Python" # using double quotes 
# In Python - there is no difference between single and double quotes

char = "C" #can also initialize only single character
multiline_str = """This is a multiline string with more than one line code."""
unicode = u"\U0001f600\U0001F606\U0001F923" # unicode characters like emojis - just use u before string(unicode characters)
raw_str = r"raw \n string" #r is used before the string like HTML code

print(string)
print(strings)
print(char)
print(multiline_str)
print(unicode)
print(raw_str)


# 3. Boolean Literal
a = True + 4  # simply 1+4 as True is considered as 1 - implicit type conversion
b = False + 10  # False means 0 

print("a:", a)
print("b:", b)


# 4. Special Literal - None - means absence of anything
a = None
print(a)

# None is used when we are sure to use a variable later but not sure when and how and where? but it might be used later 
# we can't initialize it with 0 or something as logic might get affected

c = 34+45
print(c)

# variable decla
k = None
print(k)




"""
Operators
Operators are used to perform operations on variables and 
values. Python has the following operators:

Arithmetic operators
Comparison operators
Logical operators
Bitwise operators
Assignment operators
Identity operators
Membership operators
"""

x = 5
y = 2

print(x+y)

print(x-y)

print(x * y)

print(x/y)  
print(x//y) # quotient
print(x%y) # modulus - remainder

print(x ** y) # Power
print(y**x)
print(x // 2) # integer division - quotient will be returned as integer

x=5; y=3
# Comparision Operators
print(x > y) # True as x>y 

print(x < y)

print(x >= y)

print(x <= y)

a=7  # assignment
a==7 # comparision
# diff between = and ==
print(x==y)
print(x==x)
print(x!=y)

# Logical Operators - AND , OR, etc
x =True
y = False

a= True
b = False

print(x or y) 
#OR - returns True if either one is True or both are True
print(a or b)
print(b or b)

print(x and y) # returns True when both value are true

print(not y)
print(not x)

# Bitwise - useful in binary operations like image processing project - apply filter on image after converting them to 0 & 1.

x = 2
y = 3
print(x & y) # this is Bitwise and
''' It first converts x and y i.e 2 and 3 into binary like 2's binary is 010 and 3's binary is 110 and then
use AND operator and returns the value'''

print(x | y)

print(x >> 2) #left shift

print(y << 3) # right shift

print(~x) # negation of x

# Assignment Operator
a = 3 # assigning 3 to variable a
print(a)

a=1
print(a+3)
print(a)

a=1
a = a+3   # a+=3
print(a)

a=1
print(a)
a-=3 # a=a-3  -. a=-2
print(a)

# shorthand
a+= 3 # a=a+3
# a = a + 3
print(a)
print(a -= 3) # a= a-3
print(a *= 3)
print(a &= 3)

# doesn't work in Python
print(a++)
++a


a = a + 3
a += 3
a = 3
b = 3

print(a is b)


# Identity Operators - checks if 2 variables are at same memory location

m = 4
n = 4
print(m is n)

mm = 4
nn = 5
print(mm is nn)

a = "Hello"
b = "H"
# tell me if b contains a
print(b in a)
print(a in b)
print(a is b)



# If two variables are same it doesn't mean that they are stored at same memory location
a = [1,2,3]
b = [1,2,3]

print(a is b)

a = "Hello-world"
b = "Hello-world"

print(a is not b)


# Membership Operators - whether a given variable is into other or not
# not present in other lang - Pros of Python

x = "Delhi"
print("D" in x)
print("D" not in x)

x = (1,2,3)
print(5 in x)
# applicable on list, sets,tuples, etc