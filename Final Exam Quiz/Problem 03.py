""" Following are solutions for Final Exam. """

# Final Exam - Problem 03
def dict_invert(d):
    """
    :param d: dict
    :return: An inverted dictionary.
    """
    keys = d.keys()
    keys.sort()
    values = d.values()
    # Now removing all the duplicates using Set
    finalvalues = list(set(values))

    # Here, we generate a list of lists
    # Collecting all the keys that has the same value in a list
    keylist = []
    for value in finalvalues:
        templist = []
        for key in keys:
            if d[key] == value:
                templist.append(key)
        keylist.append(templist)

    # Now removing the duplicates from the list
    # If there are more than two copies of same list
    # it means the items on that lists are the keys that have same value
    # Therefore, those duplicate lists shall be taken care of
    finalkeylist = []
    for item in keylist:
        if item not in finalkeylist:
            finalkeylist.append(item)
        else:
            finalkeylist = finalkeylist

    finaldict = dict(zip(finalvalues, finalkeylist))
    return finaldict

## Following are all test cases
# d1 = {1: 10, 2: 20, 3: 30}
# d2 = {1: 10, 2: 20, 3: 30, 4: 30}
# d3 = {4: True, 2: True, 0: True}
# d4 = {2: 3, 3: 20, 4: 10}
# d5 = {30000: 30, 600: 30, 2: 10}
# dict_invert(d4)

