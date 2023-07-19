##Lab04 Required Questions ##

_author_ = "Richard Roberts"
_credits_ = ["Module 4 Lab Sheet, Module 4 Lectures, stack overflow"]
_email_ = "Roberrf@mail.uc.edu" # Your email address

#########
# Lists #
#########

# RQ1
def cascade(lst):
    """Returns the cascade of the given list.

    >>> cascade([1, 2, 3, 4])
    [1, 2, 3, 4, 4, 3, 2, 1]
    >>> cascade([10, 12, 0, 8, 5, 3])
    [10, 12, 0, 8, 5, 3, 3, 5, 8, 0, 12, 10]
    """
    i = len(lst)
    while i > 0:
        lst = lst + [lst[i-1]]
        i -= 1
    return lst
        
# RQ2
def maptwice(fn, seq):
    """Applies fn twice onto each element in seq and returns the resulting list.

    >>> maptwice(lambda x: x*x, [1, 2, 3])
    [1, 16, 81]
    >>> maptwice(lambda x: x+20, [1, 2, 3])
    [41, 42, 43]
    """
    result = []
    for x in seq:
        result += [fn(fn(x))]
    return result

#RQ3
def filterout(pred, seq):
    """Keeps elements in seq only if they do not satisfy pred.

    >>> filterout(lambda x: x % 2 == 0, [1, 2, 3, 4])
    [1, 3]
    >>> filterout(lambda x: x + 2 == 3, [1, 4, 0, 1, 20])
    [4, 0, 20]
    """
    result = []
    for x in seq:
        if not pred(x):
            result += [x]
    return result
    

#RQ4
def comp(n, pred):
    """ Uses a one line list comprehension to return list of the first n integers (0...n-1) which satisfy the predicate pred.
    >>> comp(7, lambda x: x%2 ==0)
    [0, 2, 4, 6]
    >>> comp(10, lambda x: x*x == 9)
    [3]
    """
    return [x for x in range(n) if pred(x)]
    
#RQ5
def flatten(lst):
    """ Takes a nested list and "flattens" it.
    
    >>> flatten([1, 2, 3]) 
    [1, 2, 3]
    >>> x = [1, [2, 3], 4]      
    >>> flatten(x)
    [1, 2, 3, 4]
    >>> x = [[1, [1, 1]], 1, [1, 1]] 
    >>> flatten(x)
    [1, 1, 1, 1, 1, 1]
    >>> lst = [1, [[2], 3], 4, [5, 6]]
    >>> flatten(lst)
    [1, 2, 3, 4, 5, 6]
    """
    if len(lst) == 1:
        if type(lst[0]) == list:
            result = flatten(lst[0])
        else:
            result = lst
    elif type(lst[0]) == list:
        result = flatten(lst[0]) + flatten(lst[1:])
    else:
        result = [lst[0]] + flatten(lst[1:])
    return result

import doctest
if __name__ == "__main__":
  doctest.testmod(verbose=True)