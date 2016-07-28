
""" Following are scripts for Finger exercises in Lecture 06. """

# Lecture 06 - Problem 02

def oddTuples(aTup):
    i = 0
    collect = ()
    while i < len(aTup):
        collect += (aTup[i],)
        i += 2
    return collect

aTup = ('I', 'am', 'a', 'test', 'tuple')
print oddTuples(aTup)



# Lecture 06 - Problem 07a

testList = [1, -4, 8, -9]

def applyToeach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])

def timeFive(a):
    return a*5

applyToeach(testList, timeFive)
print testList
        
def mode(a):
    return abs(a)

applyToeach(testList, mode)
print testList

def add(a):
    return a + 1

applyToeach(testList, add)
print testList

def square(a):
    return a**2

applyToeach(testList, square)
print testList


# Lecture 06 - Problem 08

def square(a):
    return a*a

def halve(a):
    return a/2

def inc(a):
    return a+1

def applyEachTo(L, x):
    result = []
    for i in range(len(L)):
        result.append(L[i](x))
    return result


# Lecture 06 - Problem 10

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def countlist(aList):
    
    """ This function counts the number of strings or integers in
    a list. """
    
    i = 0
    for item in aList:
        if type(item) == str or type(item) == int:
            i += 1
            
    return i

def howMany(aDict):

    """ This function finds the values in a dictionary
    and counts the number of strings or integers in that value."""
    
    values = aDict.values()
    Total = 0
    for value in values:
        count = countlist(value)
        Total = Total + count
      
    return Total
    
 
print howMany(animals)


# Lecture 06 - Problem 11

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def countlist(aList):
    
    """ This function returns number of integers or strings in
    a list."""
    
    i = 0
    for item in aList:
        if type(item) == str or type(item) == int:
            i += 1
    return i


def maxvalue(aDict):
    
    """ This function counts integers or strings in each value of
    the dictionary and returns the maximum number of strings or integers in
    a value."""
    
    values = aDict.values()
    collect = []
    for value in values:
        collect.append(countlist(value))
    return max(collect)


def findvalue(aDict):

    """This function identifies the value in a dictionary with the maximum
    number of integers or strings."""
    
    values = aDict.values()
    for value in values:
        if countlist(value) == maxvalue(aDict):
            return value


def biggest(aDict):

    """ This function identifies the key associated with the value
    that has maximum number of integers or strings."""
    
    keys = aDict.keys()
    if keys == 0:
        return None
    else:
        for key in keys:
            if aDict[key] == findvalue(aDict):
                return key


print biggest(animals)
    

