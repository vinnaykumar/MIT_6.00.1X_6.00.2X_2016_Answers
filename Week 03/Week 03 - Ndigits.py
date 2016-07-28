
""" Following a solution for bonus exercise in Week 03. """



# Ndigits
# First Attempt using strings
def returnstring(x):
    return str(abs(x))

def ndigits(x):

    """
    This function counts the decimals in a given number.
    x = integer either positive or negative
    returns = an integer
    
    """
    use = returnstring(x)
    i = 0
    while use[i] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        i += 1
    return i

print ndigits(123598665.555)



# Second Attempt using divisions
def ndigits(x):
    
    """
    This function counts the decimals in a given number.
    x = integer either positive or negative
    returns = an integer
    
    """
    
    n = abs(x)
    count = 1
    while (int(n/10)) > 0:
        count += 1
        n=int(n/10)
        ndigits(n)
       
    return count

print ndigits(123598665.555)
