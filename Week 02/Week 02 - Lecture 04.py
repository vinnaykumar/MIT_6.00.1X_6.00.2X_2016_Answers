
""" Following are scripts for Finger exercises & problems in Week 02 - Lecture 04. """



# ----- Problem 03 -----
# ----------------------
def square (x):
    ''' X: int or Float.
    '''
    return x**2



# ----- Problem 04 -----
# ----------------------
def evalQuadratic (a, b, c, x):
    '''Evaluates a quadratic equation'''
    return (a*x**2)+b*x+c



# ----- Problem 05 -----
# ----------------------
def clip(lo, x, hi):
    '''
    Takes in three numbers and returns a value based on the value of x.
    Returns:
     - lo, when x < lo
     - hi, when x > hi
     - x, otherwise
    '''
    while x<lo:
        return lo
        break
        
    while x>hi:
        return hi
        break
        
    while lo<hi:
        return x
        break



# ----- Problem 08 -----
# ----------------------
def fourthpower(x):
   return square(x)*square(x)



# ----- Problem 09 -----
# ----------------------
def odd(x):
   return x%2!=0
   return False



# ----- Problem 10 -----
# ----------------------
def isVowel(char):
   return str.lower(char)=='a' or str.lower(char)=='e' or str.lower(char)=='i' or str.lower(char)=='o' or str.lower(char)=='u'




# ----- Problem 11 -----
# ----------------------
def isVowel2(char):
   vowel = ('a','e','i','o','u')
   if str.lower(char) in vowel:
      return True
   else:
      return False



