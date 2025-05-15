# Functions in Python - slides

# structure of a function with example

def is_even(number):
    """ This func tells whether given number is even or odd
    INPUT - any valid integer
    Output: even/odd
    CREATED BY: ADam
    Time: 5:20 PM IST
    This all is optional
    """
    if(type(number) == int):
        if number%2==0:
            return "Even"
        else:
            return "Odd"
    else:
        return "Not a valid integer"
is_even(679263)


def is_odd(number):
    """ This func tells whether given number is even or odd
    INPUT - any valid integer
    Output: even/odd
    CREATED BY: ADam
    Time: 5:20 PM IST
    This all is optional
    """
    if(type(number) == int):
        if number%2!=0:
            return "Odd"
        else:
            return "Even"
    else:
        return "Not a valid integer"



for i in range(1,11):
    print(i, " ", is_even(i))

# Imp: The function which doesnot have return statement, returns None

# to get its documentation
print(is_even.__doc__)
print(print.__doc__)
print(type.__doc__)


# Parameters vs Arguments - slides
# ================================================================================================================

# types of arguments

# default argument
def power(a,b):
    return a**b

power(3,2)
power(2) # error as it is expecting 2 values - here comes default arguments

def power1(a=4, b= 3):
    return a**b

power1()
power1(2,3)
power1(3)  # it by default takes b=3 when we don't give it (only 1 argument is given which will be taken for a and b by defauly will be considered 3)

# Positional Argument
power1(2,3) # argument given in order is sequentially assigned to parameters

# keyword arguments
power1(b=2, a=3) # if we give value ourself explicitly - it will be assigned as it is

# keyword arguments overwrite positional arguments - 
# basically used when we don't remember position of parameters - we give the value of useful parameters explicitly

#arbitrary arguments - which are flexible for number of arguments given - as much as much we want to give 
# e.g print function

def func(*num):# * means Python interpreter understands that this function can have multiple inputs as arguments
    """ It will take in as much arguments as we want and give the product of them"""
    product = 1
    for i in num:
        product = product*i
    print(product)

func(2,5)
func(1,2,4,6)
func(1,2,3,4,5,6)


# ========================================================================================================================
# global variable vs Local variable
def f(y):
    x=1
    x+=1
    print(x)
x=5
print(x)
f(x)
print(x)
'''
Let's analyze the code step by step:

1. `x = 5`: The variable `x` is assigned the value 5. - line 102 

2. `print(x)`: This will output `5` to the console.

3. `f(x)`: This calls the function `f` with `x` as an argument.

Now, let's look at the function `f(y)`:

1. `x = 1`: The local variable `x` is assigned the value 1 within the function `f`.

2. `x += 1`: The value of `x` is incremented by 1, so `x` becomes 2.

3. `print(x)`: This will output `2` to the console.

After the function `f(y)` has been called, we have:

4. `print(x)`: This will output `5` to the console again. The function `f(y)` did not modify the variable `x`, 
as it only works with its local `x` variable inside the function.

5. `print(x)`: This will output `5` to the console once again, as there have been no changes to the variable `x` since the 
previous `print(x)` statement.

To summarize:
- The initial value of `x` is `5`, and it remains unchanged throughout the execution.
- The function `f(y)` takes a parameter `y`, but it's not used in the function. Instead, it uses its local variable `x`.
- The function `f(y)` increments its local `x` and prints it, but it doesn't modify the variable `x` defined outside the function.
- The value of `x` remains `5` after calling the function `f(y)`.
'''

# e.g 2

def g(y):
    print(x)
    x=x+1
    print(x)
x=5
print(x)
g(x)
print(x)

'''
The code above will raise an `UnboundLocalError`. Let's understand why:

In the function `g(y)`, the variable `x` is used before it's assigned a value inside the function scope. 
This creates a scope issue with variable resolution. When Python encounters a variable in a function, 
it first looks for it in the local function scope, and only then, if not found, it looks in the global scope.

Let's analyze the code step by step:

1. `x = 5`: The variable `x` is assigned the value 5 in the global scope.

2. `g(x)`: This calls the function `g` with `x` as an argument.

Now, let's look at the function `g(y)`:

1. `print(x)`: This line will raise an `UnboundLocalError`. Python tries to print the value of the local variable `x` 
within the function, but it hasn't been assigned a value yet, so it's considered "unbound" in this context.

2. `x = x + 1`: This line will not be executed due to the error in the previous line.

3. Since an error occurred, the function `g(y)` terminates.

After calling the function `g(y)`, the program continues:

4. `print(x)`: This will output `5` to the console. The global variable `x` was not modified by the function call.

So, the output of the code will be:

```
UnboundLocalError: local variable 'x' referenced before assignment
5
```

To fix this issue, we need to explicitly declare `x` as a global variable within the function `g(y)` using the `global` keyword.

def g(y):
    global x
    print(x)
    x = x + 1
    print(x)

x = 5
g(x)
print(x)
```

With this correction, the output will be:

```
5
6
6
```

Now, the function `g(y)` uses the global variable `x`, increments it, and modifies its value. The final `print(x)` statement outside
the function will show the updated value of `x`, which is `6`.
'''

# e..g - 3

def g(y):
    print(x)
    print(x+1)
x=5
g(x)
print(x)

'''
Let's analyze the code step by step:

x = 5: The variable x is assigned the value 5 in the global scope.

g(x): This calls the function g with x as an argument.

Now, let's look at the function g(y):

print(x): This will output 5 to the console. The function g(y) accesses the global variable x, and its value is 5.

print(x + 1): This will output 6 to the console. It performs the calculation x + 1, where x is still 5, so the result is 6.

After calling the function g(y), the program continues:

print(x): This will output 5 to the console again. The value of x in the global scope remains unchanged throughout the execution.
'''
# =================================================================================================================
# Imp Note:
''''
The main difference between the two codes provided is how they handle the variable `x` within the function `g(y)`.

1. First Code:
   def g(y):
       print(x)
       x = x + 1
       print(x)
   x = 5
   g(x)
   print(x)

   Output:   UnboundLocalError: local variable 'x' referenced before assignment
             5
   In the first code, the function `g(y)` tries to access the variable `x` without declaring it as a global variable within the function
   This results in an `UnboundLocalError` because Python treats `x` as a local variable within the function scope due to the assignment
    (`x = x + 1`) inside the function. The local variable `x` is used before it's assigned a value, causing the error.

   As a result, the function `g(y)` doesn't modify the global variable `x`, and its value remains unchanged at `5`. 
   The final `print(x)` statement outside the function will show the initial value of `x`.

2. Second Code:
   def g(y):
       print(x)
       print(x + 1)

   x = 5
   g(x)
   print(x)

      Output:
   5
   6
   5
   In the second code, the function `g(y)` doesn't attempt to modify the variable `x` or reassign it. 
   It simply accesses the global variable `x` and performs calculations based on its value. Since there is no assignment inside the 
   function, Python treats `x` as a global variable without any issues.

   As a result, the function `g(y)` doesn't modify the global variable `x`, and its value remains unchanged at `5`. 
   The final `print(x)` statement outside the function will show the initial value of `x`.

In summary, the first code has an error (`UnboundLocalError`) due to a local variable resolution issue inside the function, 
while the second code works correctly and accesses the global variable `x` without any issues. Both codes, however, do not modify 
the value of the global variable `x` within the function `g(y)`.
'''


# e.g - 4

def h(y):
    x+=1  # function is trying to change the value of global variable - error -> Solution : global x
x=5
h(x)
print(x)

# Rules:
# 1. Global variable - can be used by any local function.
# 2. Local function can only use global variable, but not change it.

def h(y):
    global x
    print(x)
    x+=1 
x=5
print(x)
h(x)
print(x)




# e.g 5
# - observe the diff in 2 progarms below
def f(x): # here x is defined in local scope -> so below line is trying to update local x only
    x=x+1  # this will not change the actual value of x in global scope - just change for local scope
    print('in f(x) : x = ', x) # updated value of x is printed.
    return x
x=3
z=f(x)  # z will get the value which is returned from the function after execution
print('in main program scope : z', z)
print('in main program scope : x', x)
# -------------------------------------------------------------------------------------------------------------------------
def f(y): # error
    x=x+1  # this will not change the actual value of x in global scope - just change for local scope
    print('in f(x) : x = ', x) # updated value of x is printed.
    return x
x=3
z=f(x)  # z will get the value which is returned from the function after execution
print('in main program scope : z', z)
print('in main program scope : x', x)





# ========================================================================================================================
# Nested functions: 

def f():
    print("Inside f")

    def g():
        print("Inside g")
    g()

f() # first go to f() -> print("Inside f") then skip 2 lines and go to call g() -> print("Inside g")

g() # calling only g() shows error as g() is hidden from main program - without f() it can't execute


# Infinite loop - after a limited function call - it showed error - RAM consumption 
def f():
    print("Inside f")

    def g():
        print("Inside g")
        f()
    g()

f()


# e.g - 
def g(x):
    def h():
        x='abc'
    x=x+1
    print('in g(x) : x = ', x)
    h()
    return x  # here x = 4
x=3
z=g(x)
print(x) # global value of x doesn't change
print(z) # it will print 4 as returned form the function g(x)

# e.g - 
def g(x):
    def h(x):
        x=x+1
        print("in h(x) : x", x)
    x = x+1
    print("in g(x) : x", x)
    h(x)
    return x

x=3
z=g(x)
print("in main program scope : x = ", x)
print("in main program scope : z = ", z)

# ======================================================================================================================

x=4
y=x
print(x)
print(y)


# Everything in Python is an object - Function too

def f(n):
    return n**2

f(5)
type(f)
x=f  # now x will be same as f - it'll work exactly like f
x(2)
x(6)
f(6)

del f # deletes the func f
type(x)
x(5)

# we can store this x (function object) as an element in list
L=[1,2,3,4]
l=[1,2,3,x]
l # see x is stored as a function in this list with given mwmory address -
# we can even use it as a function
l[-1]
l[-1](6)

m = [1,2,4, x(5), 7, x(9)]
m


# ========================================================================================================================
"""
A lot more can be done with Python functions -n
Renaming a func
Deleting a func
Storing a func
Returning a func
Functions as argument in other function - see below example
"""

def func_a():
    print("inside func_a")
def func_b(z):
    print("inside func_b")
    return z()

print(func_b(func_a))














# ========================================================================================================================

# Quick exercise: What is the O/P of this code snippet?

def func1():
    return "Adam"  # it return string type

def func2():
    print("Mike")  # it returns None Type

print(func1() + " MIKE") 
print(func2() + "ADAM") 


#print(func1() + " Adam")  # it works fine as output of func1() is a string and strings can be concatenated
# print(func2() + "Mike")  # shows error as func2() returns None Type which can't be concatenated to string

