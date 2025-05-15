# Sets - datatype in Python
# rules to remember
# 1. Sets do not allow duplicates
# 2. Sets do not have indexing/slicing
# 3. Sets do not allow mutable data types(list), but strings and tuple are immutable, we can store them in a set
# 4. Sets is mutable datatype

# 2-D or 3-D sets are not possible as for that set must be inside another set but is not possible as 
# set(mutable) don't allow another mutable object in it.

# set can contain tuple, string - as tuples, string are immutable

# create sets
# empty set
s = {}
type(s) # it is dictionary not a set

s1 = set()
type(s1)

# homogeneous set
s2 = {1,2,3,5,7}
type(s2)
s3={'Adam', 4, 7.9}
type(s3)

s4 = {1,2,2,1,2,4,4,5,7,8,2}
s4 # it automatically removes the dups by internal mechanism

# ex -  
l = [1,2,21,3,2,154,1]
m = set(l)
m
type(m)


s5 = {{1,2}, [1,2]} # shows error as sets do not allow mutable datatype(set)
s5

s5 ={(1,2), (1,), 'adam'} # set can contain immutable datatype
s5
# VVI - focus on O/p- set has no indexing - order in which we give elements is not followed but
# hashing is followed - a technique to store elements in a data structure.


s6 = {[1,2,4], 'Mike'} # error because list is mutable and set do not allow mutable types
s6


#========================================================================================

# Indexing and slicing - sets doesn't support them
s2
s2[0]
s2[-1]
s2[0:4]

# we can't edit items in a set as indexing is not allowed
s2[0] = 100

# to see the memory address of a set
id(s2)

# we can't edit a set - but a trick can be used - convert the set in a list and then edit the list
# and then convert back the list into a set
# but actually we are not editing the set as when we convert the set into list -> edit it and store 
# back into a set -the new set memory address changes
s8 = {1,2,4,6,8,6}
s8
id(s8) # memory address of the set - 2342884489056
s8[0] = 344  # not possible - error
l = list(s8) # type casting - converting from one datatype to another
l
id(l) # 2342886776512 is the address of this list

# editing the list
l[0] = 100
l
set(l)

# Sample set
my_set = {1, 2, 3, 4, 5}
id(my_set) # 2342886427328
# Convert set to list using list comprehension
my_list = [x for x in my_set]
print(my_list)
my_list[0] = 100
my_list
id(my_list) # 2342887648320



# now converting back this list to set
my_set = set(my_list)
my_set
id(my_set) # now we see a changed address - 2342886429568


# sets are indeed mutable.

# Adding elements to a set using the `add()` method:

my_set = {1, 2, 3}
my_set.add(4) # adds the element at the end of set
print(my_set)

#Removing elements from a set using the `remove()` method:

my_set = {1, 2, 3, 4}
my_set.remove(3)
print(my_set)


#Updating a set with another set using the `update()` method:

my_set1 = {1, 2, 3}
my_set2 = {3, 4, 5}
my_set1.update(my_set2)
print(my_set1)

#Clearing all elements from a set using the `clear()` method:

my_set = {1, 2, 3}
my_set.clear()
print(my_set)

#Adding elements to a set using the `|` (union) operator:
my_set1 = {1, 2, 3}
my_set2 = {3, 4, 5}
my_set1 |= my_set2
print(my_set1)


# =============================================================================================
# Delete - del, remove, pop
s= {1,2,2,5,7,8,8}
s1 = {1,2,3,4,5}


s1
del s1[0] # as there is no indexing in set - so can't delete any particular item

s
del s # deletes entire set
s

s1
s1.remove(4) # to remove 4 from set s1
s1

s1.pop() # deletes the last element - last is decided as per hashing




# Set Operations
s1= {1,2,2,5,7,8,8}
s2 = {1,2,3,4,5}
s1
s2

# Concat - not possible
s1+s2

s1*3 # error - not possible in sets

# looping can be done in sets
for i in s1:
    print(i)


# membership operators work in sets
1 in s1

# functions

len(s1)
max(s1)
min(s1)

s3 = {1,2,4.7, 'Adam'}
len(s3)
max(s3) # don't work in heterogeneous sets as diff datatypes can't be compared

sum(s1)
sum(s3)


sorted(s1) # converts into list




# ===================================================================================
# there are few functions which can only be used with sets
s1
s2
s1.union(s2) # all elements from s1 and s2 - removing dups

s1.intersection(s2) # common b/w them

s1.difference(s2) # which are in s1 but not in s2
s2.difference(s1) # which are in s2 but not in s1

s1.symmetric_difference(s2) # all expect common elements in both

# disjoint - a function which return True if no element in both sets are common otherwise False
s1.isdisjoint(s2) # it's a boolean function 

s1.issubset(s2) # is s1 subset of s2

s1.issuperset(s2) # is s1 superset of s2

