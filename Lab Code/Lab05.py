_author_ = "Richard Roberts"
_credits_ = ["Module 5 lecture video, stack overflow"]
_email_ = "Roberrf@mail.uc.edu" # Your email address

## Lab 5: Required Questions - Dictionaries  ##

# RQ1
def merge(dict1, dict2):
    """Merges two Dictionaries. Returns a new dictionary that combines both. You may assume all keys are unique.
    >>> new =  merge({1: 'one', 3:'three', 5:'five'}, {2: 'two', 4: 'four'})
    >>> new == {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}
    True
    """
    result = {}
    list1 = list(dict1)
    list2 = list(dict2)
    i = 0
    run = True
    while run:
        if i < len(list1):
            result[list1[i]] = dict1[list1[i]]
        if i < len(list2):
            result[list2[i]] = dict2[list2[i]]
        if i >= len(list1) and i >= len(list2):
            run = False
        i += 1
    return result


# RQ2
def counter(message):
    """ Returns a dictionary where the keys are the words in the message, and each
    key is mapped (has associated value) equal 
    to the number of times the word appears in the message.
    >>> x = counter('to be or not to be')
    >>> x['to']
    2
    >>> x['be']
    2
    >>> x['not']
    1
    >>> y = counter('run forrest run')
    >>> y['run']
    2
    >>> y['forrest']
    1
    """
    m = message.split()
    freqtable = {}
    for x in m:
        if x not in freqtable:
            freqtable[x] = 1
        else: 
            freqtable[x] += 1
    return freqtable


# RQ3
def replace_all(d, x, y):
    """ Returns a dictionary where the key/value pairs are the same as d, 
    except when a value is equal to x, then it should be replaced by y.
    >>> d = {'foo': 2, 'bar': 3, 'garply': 3, 'xyzzy': 99}
    >>> output = replace_all(d, 3, 'poof')
    >>> output == {'foo': 2, 'bar': 'poof', 'garply': 'poof', 'xyzzy': 99}
    True
    """
    result = {}
    for x in d:
        if d[x] == 3:
            result[x] = 'poof'
        else: 
            result[x] = d[x]
    return result


# RQ4
def sumdicts(lst):
    """ 
    Takes a list of dictionaries and returns a single dictionary which contains all the keys/value pairs found in list. And 
    if the same key appears in more than one dictionary, then the sum of values in list of dictionaries is returned 
    as the value mapped for that key
    >>> d = sumdicts ([{'a': 5, 'b': 10, 'c': 90, 'd': 19}, {'a': 45, 'b': 78}, {'a': 90, 'c': 10}] )
    >>> d == {'b': 88, 'c': 100, 'a': 140, 'd': 19}
    True
    """
    freqtable = {}
    for x in lst:
        for y in x:
            if y not in freqtable:
                freqtable[y] = x[y]
            else: 
                freqtable[y] += x[y]
    return freqtable


#RQ5
def build_successors_table(tokens):
    """Takes in a list of words or tokens. Return a dictionary: keys are words; values are lists of successor words. By default, we set the first word in tokens to be a successor to "."

    >>> text = ['We', 'came', 'to', 'investigate', ',', 'catch', 'bad', 'guys', 'and', 'to', 'eat', 'pie', '.']
    >>> table = build_successors_table(text)
    >>> sorted(table)
    [',', '.', 'We', 'and', 'bad', 'came', 'catch', 'eat', 'guys', 'investigate', 'pie', 'to']
    >>> table['to']
    ['investigate', 'eat']
    >>> table['pie']
    ['.']
    >>> table['.']
    ['We']
    """
    table = {}
    prev = '.'
    for word in tokens:
        if prev not in table:
            table[prev] = []
        table[prev] += [word]
        prev = word
    return table


def shakespeare_tokens(path='shakespeare.txt', url='http://composingprograms.com/shakespeare.txt'):
    """Return the words of Shakespeare's plays as a list."""
    import os
    from urllib.request import urlopen
    if os.path.exists(path):
        return open('shakespeare.txt', encoding='ascii').read().split()
    else:
        shakespeare = urlopen(url)
        return shakespeare.read().decode(encoding='ascii').split()
    
    
shakestokens = shakespeare_tokens()
shakestable = build_successors_table(shakestokens)


def construct_tweet(word, table):
    """Returns a string that is a random sentence starting with word, and choosing successors from table.
    """
    import random
    result = ' '
    while word not in ['.', '!', '?']:
        result += word + ' '
        word = random.choice(table[word])
    return result + word


def random_tweet(table):
    import random
    return construct_tweet(random.choice(table['.']), table)


def middle_tweet(table):
    """ Calls the function random_tweet() 5 times (see Interactive Worksheet) and 
    returns the one string which has length in middle value of the 5.
    Returns a string that is a random sentence of average length starting with word, and choosing successors from table.
    """
    quotesList = []
    lengths = []
    x = 0
    while x < 5:
        s = random_tweet(shakestable)
        quotesList += [s]
        lengths += [len(s.split())]
        x += 1

    from statistics import median
    mid = median(lengths)
    x = 0
    while x < 5:
        if lengths[x] == mid:
            return quotesList[x]
        x += 1

middle_tweet(shakestable)

import doctest
if __name__ == "__main__":
  doctest.testmod(verbose=True)