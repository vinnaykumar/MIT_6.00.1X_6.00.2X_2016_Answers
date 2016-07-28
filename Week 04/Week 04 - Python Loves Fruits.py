
""" Following a solution for bonus exercise in Week 04. """

# Python Loves Fruits
def eat(fruits, letter):
    """
    Input 01 = Dictionary
    Input 02 = String (Singleton)
    Output = Dictionary
    
    This function reduces the value by 1 in the dictionary "fruits",
    associated with the key "letter"
    """
    fruits[letter] -= 1
    return fruits

def buy(fruits, letter):
    """
    Input 01 = Dictionary
    Input 02 = String (Singleton)
    Output = Dictionary
    
    This function increaes all the values by 1 in the dictionary "fruits",
    not associated with the key "letter"
    """
    
    for key in fruits:
        if key == letter:
            fruits[letter] += 0
        else:
            fruits[key] += 1
    return fruits
  
def nfruits(fruits, string):
    """
    Input 01 = Dictionary
    Input 02 = String (Sequence of characters)
    Output = Maximum value in the dictionary
    
    This function calls functions "eat", and "buy" on each letter on
    the string is that letter is not the last letter on string. If it
    is the last letter, then only function named "eat" will be called.
    """
    i = 0
    while i < len(string):
        if i != len(string)-1:
            fruits = eat(fruits, string[i])
            fruits = buy(fruits, string[i])

        if i == len(string)-1:
            fruits = eat(fruits, string[i])
            break

        i += 1

    return max(fruits.values())


