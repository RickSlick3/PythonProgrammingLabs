# CS2021 Lab 02 - Required Questions
## Modify this file by adding your salutation and code. 
## Once you pass all the doctests, then 
## you can then submit you program for credit. 

_author_ = "Richard Roberts"
_credits_ = ["N/a"]
_email_ = "Roberrf@mail.uc.edu" # Your email address

#  RQ1
"""
Write a function day_name that converts an integer number 0 to 6 into the name of a day. Assume day 0 is “Sunday”. Your function should return error message if the arguments to the function are not valid. 
"""
def day_name(n):
    """
    >>> day_name(3) 
    'Wednesday'
    >>> day_name(6) 
    'Saturday'
    >>> day_name(42)
    'Invalid argument'
    """
    if (n == 0): return 'Sunday'
    elif (n == 1): return 'Monday'
    elif (n == 2): return 'Tuesday'
    elif (n == 3): return 'Wednesday'
    elif (n == 4): return 'Thursday'
    elif (n == 5): return 'Friday'
    elif (n == 6): return 'Saturday'
    else: return 'Invalid argument'

#  RQ2
def two_of_three(a, b, c):
    """Return using one-liner x*x + y*y, where x and y are the two largest members of the
    positive numbers a, b, and c.

    >>> two_of_three(1, 2, 3)
    13
    >>> two_of_three(5, 3, 1)
    34
    >>> two_of_three(10, 2, 8)
    164
    >>> two_of_three(5, 5, 5)
    50
    """
    return ((a*a) + (b*b) + (c*c)) - (min(a, b, c)*min(a, b, c))


#  RQ3
def largest_factor(n):
    """Return the largest factor of n that is smaller than n.

    >>> largest_factor(15) # factors are 1, 3, 5
    5
    >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    40
    """
    x = (n-1)
    while (x > 0):
      if ((n % x) == 0):
        return x
      x -= 1




         
#  RQ4
""" Here we define a function main that takes a function and and a *args which is used to pass a variable number of arguments. The function main returns the application of f to *args. The first doctest should pass without modification. Add definitions for sum and mult to pass the tests."""

def main(f, *args):
    """
    >>> main(max,1,2,4)
    4
    >>> main(sum,1,2,4)
    7
    >>> main(mult,1,2,4)
    8
    """
    return f(*args)

def sum(*args):
  x = 0
  for num in args:
    x += num
  return x
def mult(*args):
  x = 1
  for num in args:
    x *= num
  return x
    

import doctest
if __name__ == "__main__":
  doctest.testmod(verbose=True)