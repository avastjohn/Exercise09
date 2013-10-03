# Factorial
def factorial(x):
    if x == 1:
        return 1
    return factorial(x-1)*x

# Multiply all the elements in a list
def multiply_all(listy):
    if listy == []:
        return 1
    return multiply_all(listy[1:])*listy[0]

listy = [6,9,5,4]

# Count the number of elements in the list l
def count_list(listy):
    if listy == []:
        return 0
    return count_list(listy[1:])+1

# Sum all of the elements in a list
def sum_list(listy):
    if listy == []:
        return 0
    return sum_list(listy[1:])+listy[0]

print sum_list(listy)

# Reverse a list without slicing or loops
def reverse(l):
    return []

# Fibonacci returns the nth fibonacci number. The nth fibonacci number is
# defined as fib(n) = fib(n-1) + fib(n-2)
def fibonacci(n):
    pass

# Finds the item i in the list l.... RECURSIVELY
def find(l, i):
    return None

# Determines if a string is a palindrome
def palindrome(some_string):
    return False

# Given the width and height of a sheet of paper, and the number of times to fold it, return the final dimensions of the sheet as a tuple. Assume that you always fold in half along the longest edge of the sheet.
def fold_paper(width, height, folds):
    return (0, 0)

# Count up
# Print all the numbers from 0 to target
def count_up(target, n):
    return