
""" Following are scripts for Finger exercises & problems in Week 04 - Lecture 07. """





# ----- Problem 06 -----
# ----------------------

def integerDivision(x, a):
    """
    x: a non-negative integer argument
    a: a positive integer argument

    returns: integer, the integer division of x divided by a.
    """
    count = 0
    while x >= a:
        count += 1
        x = x - a
    return count

print integerDivision(5,3)





# ----- Problem 07 -----
# ----------------------

def rem(x, a):
    """
    x: a non-negative integer argument
    a: a positive integer argument

    returns: integer, the remainder when x is divided by a.
    """
    if x == a:
        return 0
    elif x < a:
        return x
    else:
        return rem(x-a, a)

print rem(2,5)
print " "
print rem(5,5)
print " "
print rem(7,5)
print " "





# ----- Problem 08 -----
# ----------------------

def f(n):
   """
   n: integer, n >= 0.
   """
   if n == 0:
      return 1
   else:
      return n * f(n-1)


print f(3)
print f(1)
print f(0)




    
 
