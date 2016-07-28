
""" Following is part 02 of script for Problem Set 04 in Week 04. """
""" Please note, this script shall altered to make the game more realistic"""


from ps4a import *
import time


# Computer choses word
def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    global MaxScore
    global BestWord

    # Create a new variable to store the best word seen so far (initially None) 
    BestWord = None
    # Create a new variable to store the maximum score seen so far (initially 0)
    MaxScore = 0
    
    # For each word in the wordList
    for word in wordList:

            # If you can construct the word from your hand
            if isValidWord(word, hand, wordList)== True:

                
                # Find out how much making that word is worth
                Score = getWordScore(word, n)

                # If the score for that word is higher than your best score
                if Score > MaxScore:

                    # Update your best score, and best word accordingly
                    MaxScore = Score

                    BestWord = word


    # return the best word you found.
    return BestWord





def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    # Initial Score is 0
    TotalScore = 0

    # Whole function hinges on this condition
    while calculateHandlen(hand) > 0:
        print " "
        print "Current Hand: ", # Always remenber this
        displayHand(hand)       # It literally broke your head
        
        word = compChooseWord(hand, wordList, n)
        if word == None:
            print "Total score: " + str(TotalScore)+ " points."
            break
        else:
            TotalScore += MaxScore
            print '"'+ str(word)+'" ' + "earned " + str(MaxScore)+ " points. " + "Total: " + str(TotalScore)+ " points \n"
            hand = updateHand(hand, word)

    if calculateHandlen(hand) == 0:
        print "Total score: " + str(TotalScore)+ " points."



def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """

    # A Wrapper function to as for computer to play or to you to play
    def wrapper():

        # This while True holds the ky to this fucntion. It is the only reason this function is written.
        # Without this loop you can not come bac you raw_input after you have printed "Invalid command"
        # Always, carefully study and understand the need for this while loop
        while True:
            print " "
            say = raw_input("Enter u to have yourself play, c to have the computer play: ")

            if say == "u":
                playHand(hand, wordList, HAND_SIZE)
                return
            
            elif say == "c":
                compPlayHand(hand, wordList, HAND_SIZE)
                return

            else:
                print "Invalid command"



    # Initiating with an empty string
    prompt = " "
    while prompt != "e":
        print " "
        prompt = raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")

        # Dealing a new hand
        if  prompt == "n":
            hand = dealHand(HAND_SIZE)
            lasthand = hand
            wrapper()

        # Dealing the last hand
        if prompt == "r":
            try:
                hand = lasthand
            except UnboundLocalError:
                print "Yu have not played a hand yet. Please play a new hand first!"
            else:
                wrapper()
                    
        # End the Game
        if prompt == "e":
            break

        # Checking invalid ccharacters
        if prompt in ["a","b","c","d","f","g","h","i","j","k","l","m","o","p","q","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","0"]:
            print "Invalid command"
        
    
           


wordList = loadWords()
playGame(wordList)


