
""" Following is a script for Problem Set 01 in Week 02. """



# Counting Vowels
def countvowels(s):
    vowels = ('a','e','i','o','u')
    i = 0
    for letter in s:
        if str.lower(letter) in vowels:
            i += 1
    print "Number of vowels: " + str(i)

s='azcbobobEgghAkl'
countvowels(s)



# Counting Bob
def countbob(s):
    count = 0
    for i in range(len(s)):
        if s[i:i+3] == "bob":
            count += 1
    print "Number of times bob occurs is: " + str(count)
        
s = 'azcbobobobegghakl'
countbob(s)



# Counting and Grouping 
order = ' '

def item_order(order):
    s = order.count("salad")
    w = order.count("water")
    h = order.count("hamburger")
    return "salad:" + str(s) + " " + "hamburger:" + str(h) + " " + "water:" + str(w) 

item_order(order)


