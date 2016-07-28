
""" Following are script for bonus exercise in Week 02. """


# Polysum
import math
def polysum(n,s):

    """ This function returns the sum of area and square of the perimeter of a polygon
        n = number of sides of the polygon
        s = length of sides of the polygon
        Assumption = All sides of the polygon are of same length. """

    area = (0.25*n*s**2)/math.tan(math.pi/n) #Computing area of the polygon
    perimetersquared = (n*s)**2              #Computing the squared perimeter of the polygon
    return round(area + perimetersquared, 4) #Returning the sum of area and squaredperimeter

print "The Polysum you are looking for is " + str(polysum(47,97))
