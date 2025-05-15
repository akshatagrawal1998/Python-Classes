# Recursion in Python
# Example code for Recursion
# Factorial Calculation:**
# factorial - 7 = 7*6*5*4*3*2*1  = 7*factorial(6) = 7*6*factorial(5) = 7*6*5*factorial(4)
# factorial 0 = 1

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  # Output: 120

# Fibonacci Sequence:**

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))  # Output: 8

# Sum of a List:**

def sum_list(lst):
    if not lst:
        return 0
    else:
        return lst[0] + sum_list(lst[1:])   # 1+sum_list([2,3,4,5])  => 1+2+[sum_list([3,4,5])] => 1+2+3+sum_list([4,5])

print(sum_list([1, 2, 3, 4, 5]))  # Output: 15

# Power Calculation:**

def power(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base * power(base, exponent - 1)

print(power(2, 3))  # Output: 8

# String Reversal:**

def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return reverse_string(s[1:]) + s[0]

print(reverse_string("hello"))  # Output: "olleh"


#  Greatest Common Divisor (GCD):**

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

print(gcd(48, 18))  # Output: 6

# Counting Digits:**

def count_digits(n):
    if n == 0:
        return 0
    else:
        return 1 + count_digits(n // 10)

print(count_digits(12345))  # Output: 5


# Sum of Digits:**

def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_of_digits(n // 10)

print(sum_of_digits(12345))  # Output: 15


# Binary Search:**

def binary_search(arr, target, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, high)
    else:
        return binary_search(arr, target, low, mid - 1)

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(binary_search(arr, 6, 0, len(arr) - 1))  # Output: 5


# Palindrome Check:**

def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

print(is_palindrome("radar"))  # Output: True


# Permutations:**

def permutations(s):
    if len(s) == 1:
        return [s]
    perms = []
    for i, char in enumerate(s):
        remaining = s[:i] + s[i+1:]
        for perm in permutations(remaining):
            perms.append(char + perm)
    return perms

print(permutations("abc"))  # Output: ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']


# Ackermann Function:**


def ackermann(m, n):
    if m == 0:
        return n + 1
    if n == 0:
        return ackermann(m - 1, 1)
    return ackermann(m - 1, ackermann(m, n - 1))

print(ackermann(3, 4))  # Output: 125

# Recursive Factorial with Memoization:**

def factorial(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 0:
        return 1
    else:
        result = n * factorial(n - 1, memo)
        memo[n] = result
        return result

print(factorial(5))  # Output: 120


# Recursive List Flattening:**

def flatten_list(lst):
    flat = []
    for item in lst:
        if isinstance(item, list):
            flat.extend(flatten_list(item))
        else:
            flat.append(item)
    return flat

nested_list = [1, [2, 3, [4, 5]], 6, [7, 8]]
print(flatten_list(nested_list))  # Output: [1, 2, 3, 4, 5, 6, 7, 8]
