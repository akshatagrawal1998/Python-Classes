# Tuples in Python - similar to list - data structure
# tuples are immutable while list are mutable - we can't edit a tuple once created
# we can read from tuples but not write - it's a read only datatype
# Application - used where data need not to be changed - e.g historical data of a college


#create tuples - we use () not [] to create tuple
t=()
t
type(t)

# homogeneous tuple
t1 = (1,2,34,5)
t1

# heterogeneous tuple - containing more than one datatype
l2 = (1,'Adam', 5.6)
l2

# 2-D tuple
t_2 = ((1,2), (4,6), 8)
type(t_2)
type(t_2[0])

# single item tuple 
l3 = (4)
type(l3)  #  int type not tuple
# we have to use comma to create a single item tuple
l4 = (4,)
type(l4)

int(4.3)

# using type conversion method to create tuple
t6 = tuple("Goa")   # t6 = ("Goa",)
t6
type(t6)

t66 = ('G', 'O', 'A')
type(t66)

# tuple from a list
t7 = tuple([1,2,4,5,'Adam'])
t7
type(t7)

# Access items from a tuple
t7
t7[-1]
t7[2]

# we can store a tuple inside a list and vice versa
y = [1,2,4, (1,3)]
type(y)

z =(1,2,4,[34,75])
type(z)


# Difference with list comes in editing elements 
l = [1,2,3,5]
l
l[0] = 100
l


t=(1,2,3,4)
t[0] = 100  # shows error
t

# Basically Tuples are immutable - can't change - it is like string
# neither we can add elements nor edit elements in it

# Deleting from tuple
t
del t[0]
del t 
# we can delete the whole tuple only - but we can't delete a single or multiple elements from it

# operations in tuple
t1 = (1,2,3)
t2 = ('Adam', 'Mike',3)
t1+t2
t1*3
t2*3
2 in t2
2 in t1

for i in t1:
    print(i)

# Functions in tuple
len(t1)
sum(t1)
min(t1)
max(t1)
sorted(t1, reverse=True) # it'll convert into a list when we sort a tuple
t1.sort() # tuple doesnot any attribute called sort()


str = "Adam"
str*2


