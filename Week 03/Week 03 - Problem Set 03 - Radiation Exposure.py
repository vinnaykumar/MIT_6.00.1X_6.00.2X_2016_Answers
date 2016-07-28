
""" Following is a script for Problem Set 03 in Week 03. """



# Radiation Decay
def f(x):
    
    """
    This function calculates the value of a point
    on the decay curve.

    """
    
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)



def radiationExposure(start, stop, step):
    
    """
    Computes and returns the amount of radiation exposed
    to between the start and stop times. Calls the 
    function f (defined for you in the grading script)
    to obtain the value of the function at any point.
 
    start: integer, the time at which exposure begins
    stop: integer, the time at which exposure ends
    step: float, the width of each rectangle. You can assume that
    the step size will always partition the space evenly.

    returns: float, the amount of radiation exposed to 
    between start and stop times.
    """
    # Multiplier needs to be calculated very carefully. All the calculation hinges on it
    multiplier = (stop - start) / step
    i = 0
    total = 0
    while i < multiplier:
        exposure = f(start)*step
        start = start + step
        i += 1
        total = total + exposure
    return total
    
    
print radiationExposure(40,100,1.5)






    
