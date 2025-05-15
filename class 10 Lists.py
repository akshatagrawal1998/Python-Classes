# Lists in Python

# List is a data structure in Python similar to array in other Programming language.
# Array is homogeneous while List can be heterogeneous.
# Arrays are continuous (elements are stored one after other) - Lists are not
# So Arrays are faster than List - fetching element from a sequence is fast
# Lists in Python are mutable
# Lists are ordered




# Create Lists

# 1. Empty List -
L = []
print (L)
type(L)


# 2. Homogeneous list
Li = [1,2,3,4,6]
Li

# Heterogeneous lists
list = [1, "Adam", "Michel", 4.6, True, 6+7j]
list
type(list)


# multidimensional list
l = [1,2,4, [4, 'Adam']]   # 2D list
print(l)
l[0]
l[3]
l[3][0]
l[3][1]
len(l)


# 3D list - a list containing another list which has another list inside it
list_3D = [[[1,2,3], [['Adam', 'Mike'], ['x', 4.5]]]]
list_3D
list_3D[0][1][0][0]

list_3D[0]   # [[1, 2, 3], [['Adam', 'Mike'], ['x', 4.5]]]
list_3D[0][0]
list_3D[0][1]  # [['Adam', 'Mike'], ['x', 4.5]]
# [['Adam', 'Mike'], ['x', 4.5]]
list_3D[0][1][0]  # ['Adam', 'Mike']
list_3D[0][1][0][0]



# Access items from a list  - similar as string indexes

l2 = [1,2,3,4,'Adam']  # indexing starts from 0
l2[2]
l2[-1]

# from multidimensional list
l = [1, 2, 4, [4, 'Adam']]
l
l[-1]
l[-1][0]
l[-1][1]

list_3D
list_3D[0][1][0][1]


# edit a list
l
# Lists in Python are mutable - we can edit a list
l[0] = 'Mike'
l

Li
Li[1:4] = [200,300,500]
Li

# Add items to list
# append, extend, insert

Li
Li.append(1001) # adds only one item at last of the list
Li
Li.append([1,2])
Li
Li.append(1,2) # gives an error because append takes only one argument.
Li.append(2)

# add multiple items at last to a list
Li.extend([4000,6000,8000])
Li

Li.extend('Goa')  # focus that if only 1 item is passed in extend func - it converts into individual letters
Li
Li.extend(['Mumbai']) # add Mumbai as it is at the last of the list
Li

# insert anywhere in the list by telling the index position
Li.insert(1, 'Nice')
Li
Li.insert(1, ['Nice', 'Adam', 'Mike'])
Li.insert(0, 'Mike')


# Delete from list
# 4 ways -  del, remove, pop, clear
Li
# del keyword deletes the element at given index
del Li[-1]
Li
del Li[-3:] # from -3 till end
Li


# Remove - when we don't know the index position but we know the element to be removed
Li 
Li.remove('Nice') # it shows error if the element is not present in the list
Li


# pop - deletes the element at last
Li
Li.pop()
Li

# clear() - empties the list
l
l.clear()
l


# Operations in List

n = [1,2,3,4]
m = [3,'Adam']
n+m  # concatenation - it creates a new list altogether - neither m nor n is updated.

# list multiplication
m*5
n*3


# loops in list
for i in n:
    print(i)

# list_3D
for j in list_3D:
    print(j)


# membership operator
3 in list_3D

[1,2,3] in list_3D
([[1,2,3]]) in list_3D

[[[1,2,3]]] in list_3D

for i in list_3D:
    for j in i:
        print(j)


(['Adam', 'Mike'], ['x', 4.5]) in list_3D

# functions in List

Li = [3,67,2,1,75,98,34, 34, 34]
type(Li)
len(Li)
min(Li)
max(Li)
sorted(Li) # default = ascending
sorted(Li, reverse=True) # descending

Li
# sorted is not a permanent operation - original list still remains same
# sort is another function which is a permanent operation

Li
Li.sort()
Li
Li.sort(reverse=True)
Li

# Index in List
Li.index(5000)  # li is the list in which we want to get the index of 5000
Li.index(34)


# Quick exercise

str = "Adam is a good man"
str
str.title()
# w/o using title function let's do the same thing - 






str.split() # now it is a list of each word - string to list
str[0]
str
s = str.split()
s

for i in s:
    print(i.capitalize())

# Now let's convert it back to string
new_list = []
for i in s:
    new_list.append(i.capitalize())

new_list
print(" ".join(new_list))

# Now we have our title functiontask achieved w/o it


# Exercise 2:
s = "abc@gamil.com"
# find the characters before @
position = s.find("@")
position
s[0:position]

# way 2
s.split("@")
s.split("@")[0]

# Exercise 3: remove dups from a list
l = [1,2,4,1,3,5,6,3,1,2]
l
# way 1 
l1 = [] # empty list
for i in l:
    if i not in l1:
        l1.append(i)

print(l1)

# way 2
set(l)

