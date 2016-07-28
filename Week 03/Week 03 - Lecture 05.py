
""" Following are scripts for Finger exercises & problems in Week 03 - Lecture 05. """



# ----- Problem 01 -----
# ----------------------
def iterPower(base, exp):

    """ Base: int ot flot.
        exp: int >= 0

        returns: int or float, base^exp """

    result = 1
    while exp >0:
        result *= base
        exp -= 1
    return result

print iterPower(2.2,3)


# Lecture 05 - Problem 02
def recurPower(base, exp):

    """ Base: int ot flot.
        exp: int >= 0
        returns: int or float, base^exp """

    if exp == 0:
        return 1
    return base*recurPower(base, exp-1)

print recurPower(-8.6,6)


# Lecture 05 - Problem 03
def recurPowerNew(base, exp):

    """ Base: int ot flot.
        exp: int >= 0
        returns: int or float, base^exp """

    if exp == 0:
        return 1
    if exp%2 == 0:
        return recurPowerNew(base*base, exp/2)
    if exp%2 != 0:
        return base*recurPowerNew(base, exp-1)


print recurPowerNew(1.14,6)


# Lecture 05 - Problem 04
def gcdIter(a,b):
    c = min(a,b)
    while c > 0:
        if a%c==0 and b%c==0:
            return c
        c -= 1
    return c

print gcdIter(17,12)


# Lecture 05 - Problem 05
def gcdRecur(a,b):
    if b == 0:
        return a
    else:
        return gcdRecur(b, a%b)

print gcdRecur(17,12)


# Lecture 05 - Problem 06
def lenIter(aStr):
    i = 0
    for letter in aStr:
        i += 1
    return i

print lenIter(aStr)


# Lecture 05 - Problem 07
def lenRecur(aStr):
    
    if aStr == '':
        return 0

    return 1 + lenRecur(aStr[1:])


print lenRecur(aStr)


# Lecture 05 - Problem 08
def isIn(char, aStr):

    if len(aStr) == 1 and aStr == char:
        return True
    else:
        False
        
    if char == aStr:
        return True
    
    if aStr == '':
        return False
    
    if aStr[len(aStr)/2] == char:
        return True

    if char < aStr[0]:
        return False

    if char > aStr[-1]:
        return False

    
    if aStr[len(aStr)/2] > char:
        return isIn(char, aStr[:len(aStr)/2])


    if aStr[len(aStr)/2] < char:
        return isIn(char, aStr[len(aStr)/2:])


print isIn(char, aStr)


# Lecture 05 - Problem 09   
def semordnilapWrapper(str1, str2):

    if len(str1) == 1 or len(str2) == 1:
        return False
    if str1 == str2:
        return False
    return semordnilap(str1, str2)

def semordnilap(str1, str2):

    if len(str1) != len(str2):
        return False

    if str1 == str2:
            return True
        
    if str1[0] == str2[-1]:
        return semordnilap(str1[1:], str2[:-1])
    else:
        return False

print semordnilapWrapper(str1, str2)

    

