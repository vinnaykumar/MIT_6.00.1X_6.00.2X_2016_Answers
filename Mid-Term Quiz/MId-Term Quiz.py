
""" Following are scripts for Finger exercises & problems in Mid-Term quiz. """





# ----- Problem 04 -----
# ----------------------

def isPalindrome(aString):

    """
    Takes a string as an argument and
    checks whether it is a valid Palindrome
    returns True or False
    """
    Length = len(aString)

    # For words in which the total number of letters is Even
    if Length % 2 == 0:
        # Establishing limits for counters
        iLimit = ((Length / 2.0)- 1)+1
        jLimit = ((Length / 2.0)*-1)-1
        i = 0
        j = -1
        Count = 0

        while i < iLimit and j > jLimit:
            if aString[i].lower() == aString[j].lower():
                Count += 1
            i += 1
            j -= 1

        if Count == Length / 2.0:
            return True
        else:
            return False

    # For words in which the total number of letters is Even      
    elif Length % 2 != 0:

        # Vey Important Step
        Length = Length - 1
        # Establishing limits for counters
        iLimit = ((Length / 2.0)- 1)+1
        jLimit = ((Length / 2.0)*-1)-1
        i = 0
        j = -1
        Count = 0

        while i < iLimit and j > jLimit:
            if aString[i].lower() == aString[j].lower():
                Count += 1
            i += 1
            j -= 1

        if Count == Length / 2.0:
            return True
        else:
            return False





# ----- Problem 05 -----
# ----------------------

def dotProduct(listA, listB):
    """
    Multplies all the items in listA to items
    at similar location in listB and returns
    a Sum.
    Input(listA) = A list of integers
    Input (listB) = A list of integers
    """
    Count = len(listA)
    i = 0
    Result = []
    while i < Count:
        Match = listA[i]*listB[i]
        Result.append(Match)
        i += 1
    return sum(Result)





# ----- Problem 06 -----
# ----------------------

def flatten(aList):
    """
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList
    This is a good example to understand the use of Recursion
    """
    Catch = []
    for item in aList:
        if type(item) == type([]):
            # This is very important
            # Make sure you remember the difference between
            #'Extend' and 'Append.'
            # That is the key here
            Catch.extend(flatten(item))
        else:
            Catch.append(item)
    return Catch





# ----- Problem 07 -----
# ----------------------

def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    Common = []
    Unique = []
    CommonValues = []
    UniqueValues = []

    # Extracting keys common in both the dictionaries
    for key in d1:
        if key in d2:
            Common.append(key)
        else:
            Unique.append(key)
            
    # Extracting keys unique in both the dictionaries
    for key in d2:
        if key not in d1:
            Unique.append(key)

    # Applying function "f" to common keys and catching
    # function "f" could be defined in anyway
    # resulting values
    for item in Common:
        Value = f(d1[item], d2[item])
        CommonValues.append(Value)

    # Extracting all the values associated with the
    # Unique keys
    for item in Unique:
        if item in d1:
            UniqueValues.append(d1[item])
        elif item in d2:
            UniqueValues.append(d2[item])

    # Making dictionaries
    # This "zip" method is important
    d01 = dict(zip(Common , CommonValues))
    d02 = dict(zip(Unique, UniqueValues))

    # Returnig a Tuple
    return d01, d02



# Sample "f" function
def f(a,b):
    return a>b





# ----- Problem 08 -----
# ----------------------

def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements. Remaining elements in L
            should be in the same order.
    Returns the length of L after mutation
    """
    # Initiating a list to capture all the strings for which
    # the function will return "False"
    Remove = []

    # This variable is created to check whether there are any
    # strings in L for which function "f" will return "False"
    # If this value is zero the length of original L is returned
    IfFalseValue = 0

    # Checking strings for their output from function "f"
    # Values for which function "f" returns "False" are appened
    # to the "Remove" list
    for i in range(0, len(L)):
        if f(L[i]) == False:
            IfFalseValue = 1
            Remove.append(L[i])

    # Only if this value of this variiable is 1
    # L will be mutated
    if IfFalseValue == 1:
        for i in range(0, len(Remove)):
            L.remove(Remove[i])
            
    return len(L)

# Sample function to test code to be deleted before pasting
def f(s):
    return 'a' in s

# Sample list to be deleted  
L = ['a', 'b', 'a']
# Sample function call to be deleted
print satisfiesF(L)
# Sample print statement to be deleted
print L

# The codes asks to run call this function
run_satisfiesF(L, satisfiesF)


