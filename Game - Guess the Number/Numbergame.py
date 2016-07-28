
""" Following are scripts for a fun number guesssing game developed in Week 02 - Lecture 03. """


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
    
 
