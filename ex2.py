# Write a Python program to find the sum of all elements in a list.

# find whether the given string contains the world data

str = """Data analysis is the process of examining, cleaning, transforming, and interpreting large sets of data to extract meaningful 
insights. It involves using statistical methods, machine learning algorithms, and visualization techniques to discover patterns, 
trends, and correlations. Effective data analysis enables informed decision-making, identifies opportunities, and addresses challenges
across various domains."""

print(str)

# There is a string in Python called "str" Check if that string contains the word "data"
print("data" in str)  # shift + enter



# Write a Python program to check if a given number is even or odd.
num = int(input("Enter the number to be checked for Even or Odd"))
if num%2 == 0:
    print("Even")
else:
    print("odd")


num = [1,2,3,4,5,6,7,8,9,2,414,25,214,44,2132,2,43,55]
for a in num:
    if a%2==0:
        print(a, "Even")
    else:
        print(a, "Odd")

l = ["ABC", "XYZ", "MNO"]
for i in l:
    print(i)

s1 = {1,2,3,5,7}
s2 = {4,5,67,21,2}
for i in s1:
    if i in s2:
        print(i)

# to find the minimum element in a list
l = [1,3,6,3,87,34,12,43,2]
min = l[0]
for i in range(1,len(l)):
    if(l[i] < min):
        min = l[i]
print(min)

l = [1,3,6,3,87,34,12,43,2]
print(min(l))

l = [1, 3, 6, 3, 87, 34, 12, 43, 2]
min_val = min(l)
print(min_val)


l = [1,3,6,3,87,34,12,43,2]
print(max(l))

# to find the maximum element in a list
max = 0
l = [1,3,6,3,87,34,12,43,2]
for i in len(l):
    if(l[i] > l[i+1]):
        max = l[i]
    else:
        max = l[i+1]
print(max)


sum=0
l = [1,4,7,3,2,53,123,643,78]
for i in range(len(l)):
    sum = sum+l[i]

print(sum)

i=0
sum=0
l = [1,4,7,3,2,53,123,643,78]
while(i<=len(l)):
    sum = sum+l[i]

print(sum)


range(1,10)
# Prime numbers
count = 0
num = 7
for i in range(1,num+1):
    if(num%i) == 0:
        count = count+1

if (count == 2):
    print("prime")
else:
    print("Not prime")
    

/*
# 7 - 1,2,3,4,5,6,7
7%1 = 0 True   count = 0+1 = 1
7%2 = 0 False  count = 1
7%3 = 0 False  count = 1
7%4 = 0 False  count = 1
7%5 = 0 False  count = 1
7%6 = 0 False  count = 1
7%7 = 0 True  count = 1+1  = 2


5 % 1 = 0 count = 1
5%2 = 0 false count=1
5%3 = 0 false count=1
5%4 = 0 false count=1
5%5 = 0 false count=1+1 = 2
*/


t = (1,2,3,6,3,21)
for i in range(0 : len(t)):
print(i)