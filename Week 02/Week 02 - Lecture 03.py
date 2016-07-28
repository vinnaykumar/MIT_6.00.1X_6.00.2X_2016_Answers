
""" Following are scripts for Finger exercises & problems in Week 02 - Lecture 03. """



# ----- Problem 02 -----
# ----------------------

# Part 2a
num = 2
while num < 12:
    print num
    num += 2
print "Goodbye!"

# Part 2b
print "Hello!"
num = 10
while num > 0:
    print num
    num -= 2
    
# Part 2c
count = 1
num = 0
while count < end+1:
    num +=count
    count +=1
print num 



# ----- Problem 05 -----
# ----------------------

# Part 5a
for i in range(2,11,2):
    print i
print "Goodbye!"

# Part 5b
print "Hello!"
for i in range(10,0,-2):
    print i

# Part 5c
num = 0
for i in range (1,end+1):
    num += i
print num



# ----- Problem 09 -----
# ----------------------
print "Please think of a number between 0 and 100! "
prompt = " "
low = 0
high = 100
ans = (high + low) // 2

# This while loop is important just to keep the scipt running.
# Everything hinges on this while loop for the program to keep running.
while prompt != 'c': 
    print " "
    print "Is your secret number " + str(ans) + "? "
    print " "

    prompt = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")

    if prompt != "c" and prompt != "h" and prompt != "l":
        print " "
        print "Sorry, I did not understand your input."

    if prompt == "c":
        print " "
        print "Game over. Your secret number was: " + str(ans)
        break

    if prompt == "h":
        high = ans

    if prompt == 'l':
        low = ans
    
        
    ans = (high + low) // 2
    
 
