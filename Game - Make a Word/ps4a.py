
""" Following is part 01 of script for Problem Set 04 in Week 04. """
""" Please note, this script shall altered to make the game more realistic"""


import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}


WORDLIST_FILENAME = "words.txt"



def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    return wordList


wordList = loadWords()


def getFrequencyDict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq



def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    score = 0
    for letter in word:
        score += SCRABBLE_LETTER_VALUES[letter]
    if len(word)==n:
        return score*len(word)+50
    else:
        return score*len(word)



def displayHand(hand):
    """
    Displays the letters currently in the hand.

    For example:
    >>> displayHand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
             print letter,               # print all on the same line
    print 



def dealHand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    numVowels = n / 3
    
    for i in range(numVowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(numVowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand



def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    updatedhand = hand.copy()
    for letter in word:
        if updatedhand[letter] == 0:
            updatedhand[letter] -= 0
            return updatedhand
        if updatedhand[letter] != 0:
            updatedhand[letter] -= 1

    return updatedhand



def makestring(hand):
    """
    This function takes one hand and returns a string of all letters
    in the hand. This is a custom fucntion written by Devang. Not originally
    proposed in the problem set.

    """
    make = []
    for key in hand.keys():
        make.append(key*(hand[key]))
    return "".join (make)



def checkword(word, hand):
    """
    This function evaluates whether all the letters of word are in
    the hand. This is a custom fucntion written by Devang. Not originally
    proposed in the problem set.

    """
    # First Test: Checking if all the letters in the word are also in the hand
    # Conducting this test with a counter
    i = 0
    FirstCount = 0
    for i in range (len(word)):
        if word[i] in makestring(hand):
            FirstCount += 1
        else:
            FirstCount += 0
        i += 1
            
    # Second Test: Checking if occurencces of all the letters in the word matches the occurrences in the hand
    # Conducting this test with a counter
    SecondCount = 0
    for i in range (len(word)):
        if word.count(word[i]) == makestring(hand).count(word[i]):
            SecondCount += 1
        else:
            SecondCount += 0
        i += 1
            
    # Final Test: If First and Second test are successful and if the length of the word is less than or equal to the length of the string
    # generated from hand
    if len(word) == FirstCount and len(word) == SecondCount and len(word) <= len(makestring(hand)):
        return True
    else:
        return False



def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    # This function is totally altered from what was proposed in the original problem set
    if checkword(word, hand) == True and word in wordList:
        return True
    else:
        return False



def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    return sum(hand.values())



def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """
    # Initiating the TotalScore
    TotalScore = 0

    # The whole scripts hinges on this checking of length of hand
    while calculateHandlen(hand) != 0:
        print " "
        print "Current Hand: ",
        displayHand(hand)

        # Takiing user input
        word = raw_input('Enter word, or a "." to indicate that you are finished: ')
        
        # If the user enters "." Game aborted.
        if str(word) == ".":
            print "Goodbye! Total Score: " + str(TotalScore) + " points."
            break
        
        # Checking is the word is valid. If yes, then getting scores    
        if isValidWord(word, hand, wordList) == True:
            WordScore = getWordScore(word, n)
            TotalScore += WordScore
            print '"'+ str(word)+'" ' + "earned " + str(WordScore)+ " points. " + "Total: " + str(TotalScore)+ " points"
            print " "
            hand = updateHand(hand, word)
            
        # If entered word is not valid then throwing a message to that effect
        else:
            print "Invalid word, please try again."
            print " "
            
        # If all the letters in the hand are used, End of the Game.
        if calculateHandlen(hand) == 0:
            print "Run out of letters. Total score: " + str(TotalScore)+ " points."



def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1    
    """
    # Initiating with an empty string
    prompt = " "
    while prompt != "e":
        print " "
        prompt = raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")

        # Dealing a new hand
        if  prompt == "n":
            hand = dealHand(HAND_SIZE)
            lasthand = hand
            playHand(hand, wordList, HAND_SIZE)

        # Dealing the last hand
        if prompt == "r":
            try:
                hand = lasthand
            except UnboundLocalError:
                print "Yu have not played a hand yet. Please play a new hand first!"
            else:
                playHand(hand, wordList, HAND_SIZE)

        # End the Game
        if prompt == "e":
            break

        # Checking invalid ccharacters
        if prompt in ["a","b","c","d","f","g","h","i","j","k","l","m","o","p","q","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","0"]:
            print "Invalid command"




##playGame(wordList)
