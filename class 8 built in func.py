# Important Built In Functions in Python - 

# 1. print
print("Hello world")

# 2. input
input("Enter your name")

# 3. type
a = True
type(a)

# 4. int etc.
int(5.6)
# float
# str
# list
# tuple


# 5. abs - gives the absolute value of given integer
abs(-4)


# 6. pow
pow(2,-3) # power of 2 raise to the power -3
pow(2,3)
print(2**3)
# 7. min/max
min("kolkata") # based on ASCII characters - a has min ASCII value
'a'


# 8. round
c = 22/7
round(c)
print(round(c,2))


print(5//2)
print(5%2)
#9. divmod - returns a tuple - quotient and remainder
divmod(5,2)  # / return quotient and % returns remainder
divmod(10,3)
divmod(100,10)


#10. bin/oct/hex - get binary, octadecimal or hexadecimal equivalent of given number
hex(4) # base = 16
bin(2) # base = 2
oct(5) # base = 8

# 11. id - address of the variable in memory in my computer - urs may be different
a = 3
id(a)
print(a)


# 12. ord - returns the ASCII code of a character
ord('A')
ord('a')
ord('K')

# 13. len - length of any iterable object - string, list, tuple, set, etc
len([1,2,3])
len({'Adam','Mike', 'julie'})
len("Adam")
len(["Adam", "Julie", "Mike"])


# 14. sum
# s[2] = 3
s=[1,2,3,4,5]
len(s)
sum=0
for i in range(0,len(s)): # range(0,5) = 0,1,2,3,4
    sum = sum + s[i] # 0+1 = 1   # 1+2 = 3   # 3+3 = 6 +

print(sum)

s=[43,231,643,123,64]
print(s[0])
print(s[1])
print(s[3])
print(s[4])
print(s[5])


sum({1,2,3,4,5})


# 15. help
help('print')
print()
help('sum')