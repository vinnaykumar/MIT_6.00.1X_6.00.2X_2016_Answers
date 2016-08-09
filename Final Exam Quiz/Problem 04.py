""" Following are solutions for Final Exam. """


# Final Exam - Problem 04 - Part 01
def getSublists(L, n):
    """
    :param L: A list of integers
    :param n: An integer
    :return: A list of lists
    """
    i = 0
    k = 0
    masterlist = []
    while i < len(L)- n + 1:
        k = n + i
        sublist = L[i:k]
        masterlist.append(sublist)
        i += 1
        k += 1
    return masterlist

## Following are the test cases
# L1 = [10, 4, 6, 8, 3, 4, 5, 7, 7, 2]
# n1 = 4
# L2 = [1, 1, 1, 1, 4]
# n2 = 2
# getSublists(L2,n2)


# Final Exam - Problem 04 - Part 02 Helper Function
def checkincrease(L):
    """
    :param L: A list of integers
    :return: True if every item in the list is smaller than the next item
    else return False
    """
    i = 0
    Total = 0
    while i < len(L) - 1:
        if L[i] <= L[i+1]:
            Total += 1
        else:
            Total += 0
        i += 1

    if Total + 1 == len(L):
        return True
    else:
        return False


# Final Exam - Problem 04 - Part 02
def longestRun(L):
    """
    :param L: A list of integers
    :return:
    """
    catchlist = []
    k = len(L)
    while k > 0:
        # For every value of k create lists
        # Using the getSubist function
        checklist = getSublists(L, k)
        for item in checklist:
            # For all the list generated
            # If checkincrease function returns True
            # Then we catch the length of those lists
            if checkincrease(item) == True:
                catchlist.append(len(item))
        k -= 1
    # Finally taking the length of the longest list
    return max(catchlist)

## Following are some test cases
# L = [0]
# L1 = [2,5,6,9,12,13,15]
# L2 = [-10, -5, 0, 5, 10]
# print "Answer " + str(longestRun(L))

