# dictionary in Python
# items are stored as key value pair

# rules to remember
# 1. keys should always be immutable while values can be mutable
# 2. Dictionary do not have indexing/slicing like sets
# 3. Keys should be unique
# 4. dictionary is mutable datatypes

# Mutable - list, sets, dictionary
# Immutable - string, tuple, int, float, boolean, complex

# create dictionary
d1 = {}
type(d1)

d = {'name':"Adam", 'Gender': 'Male'}
d
type(d)


# 1. keys should always be immutable while values can be mutable - let's try to use list(mutable) as key
d2 = {[1,2,3] : "Adam"}  # list can't be used as key as it is mutable and keys are always immutable
# key:value

d3 = {(1,2,3) : "Adam"} # tuple can be used as key as it is immutable
type(d3)

# keys should be unique
d4 = {'name' : 'rahul', 'gender' : 'male' , 'name' : 'Adam'}
# error won't come but latest value of the key will be stored as an updation step
d4
type(d4)

# ==================================================================================================
# 2-D dictionary
d3 ={"name":"Eve", "marks" : {"English" : 79 , 'maths' : 89}}
d3
d3['marks']['English']


d4 ={"name":"Eve", "marks" : {"English" : 79 , 'maths' : {'Part1' : 78 , 'Part2' : 56}}}
d4
type(d4)

# -==================================================================================================
# Accessing items from a dictionary is done using it's key
# dictionary doesn't have indexing - so accessing elements can be done using key
d4['name']
d3["marks"]


d4['marks']
d4['marks']['maths']
d4['marks']['maths']['Part2']


# =================================================================================================
# edit a dictionary

d3
d3['name'] = "Adam"
d3

# add new key value pair
d3['Age'] = 32
d3

# =================================================================================================
# delete in dictionary - del, clear

del d3

# we can also delete individual key value pair
d4
del d4['name']
d4

d4.clear() # dict becomes an empty dictionary
d4


# =================================================================================================
d1 = {'name' : "Mike", "age" : 56}
d2 = {"marks" : 56}

# concat of dict not possible
# multiplication not possible

# loops
for i in d1:
    print(i)
# above loop will give us keys only

# to get values - 
for i in d1:
    print(i," ", d1[i])

# membership operators in dictionary - it checks for keys not values
'Mike' in d1
"name" in d1
"Name" in d1


# =================================================================================================
# Functions in dict

len(d1)
max(d1) # based on ASCII characters
min(d1)


# Sum won't work for string datatype, but if keys were of numerical type then sum can work

sorted(d1, reverse = True)


# To get all the keys or all values in a dictionary
d3
d3.keys()
d3.values()