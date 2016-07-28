
""" Following is a script for Problem Set 03 in Week 03. """



# Hangman game
import random
import string

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
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
    False otherwise. This function is not used at all.
    '''
    i = 0
    collect = []
    while i < len(secretWord):
        
        check = secretWord[i] in lettersGuessed # Checking if the letter is in lettersGuessed
        collect.append(check)                   # Making a list of boolean outputs
        i += 1
   
    if collect.count(True) == len(secretWord):  # If the time number of times TRUE appears in collect is equal to the length of secretWord
        return True
    else:
        return False


def getGuessedWord(secretWord, lettersGuessed):
    
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
    what letters in secretWord have been guessed so far.
    This is a very important function.
      
    '''
    i = 0
    collect = []
    while i < len(secretWord):
        
        if secretWord[i] in lettersGuessed: # Checking is the letter is in lettersGuessed
            letter = secretWord[i]
            collect.append(letter)          # Collect letters in a list called "Collect"
        else:
            collect.append("_ ")            # Also, Collect "_" in a list called "Collect"
        i += 1
        
    collect                                 # Final list
    
    flattenedlist = ''.join(collect)        # Coverting list to String
    return flattenedlist
                  

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    collect = []
    import string
    fullstring = string.ascii_lowercase

    for letter in fullstring:
        if letter not in lettersGuessed:
            letterlist = letter        # Collecting the letters not in lettersGuessed
            collect.append(letterlist)
    
    collect # Final list
    flattenedlist = ''.join(collect)   # Converting list to string
    return flattenedlist


def ifletterinsecret(lettersGuessed,secretWord):

    """
    This function checks whether the last entered letter
    is in the secretWord. A very important function
    """
    
    if lettersGuessed[-1] in secretWord:
        return True
    else:
        return False



def hangman(secretWord):
    
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    
    print "Welcome to the game, Hangman!"
    print "I am thinking of a word that is " +str(len(secretWord))+" letters long."
    print "_ _ _ _ _ _ _ _ _ _ _ _ \n"

    lettersGuessed = []
    Guesses = 8
    while Guesses > 0:
        
        print "You have " + str(Guesses) + " guesses left. "
        print "Available letters: " + getAvailableLetters(lettersGuessed)
        Guessed = raw_input("Please guess a letter: ")
        Guessedlower = Guessed.lower()
        lettersGuessed.append(Guessedlower) # Every guessed letter is added to the list named lettersGuessed
        
        # Following code block handles repititive entry of letters
        if len(lettersGuessed) != 1 and lettersGuessed.count(lettersGuessed[-1]) > 1: # Checking if last entered letter occurs more than once in the list
            print "Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed)
            Guesses = Guesses - 0
            print "_ _ _ _ _ _ _ _ _ _ _ _\n"
            
        # Following code block handles correct entry of letters
        if lettersGuessed.count(lettersGuessed[-1]) == 1:    
            if ifletterinsecret(lettersGuessed,secretWord) == True:
                print "Good guess: " + getGuessedWord(secretWord, lettersGuessed)
                if getGuessedWord(secretWord, lettersGuessed) == secretWord:
                    print "_ _ _ _ _ _ _ _ _ _ _ _ \n"
                    print "Congratulations, you won!"
                    break
                Guesses = Guesses - 0
                print "_ _ _ _ _ _ _ _ _ _ _ _ \n"
                
        # Following code block handles wrong entry of letters
        if lettersGuessed.count(lettersGuessed[-1]) == 1:            
            if ifletterinsecret(lettersGuessed,secretWord) == False:
                print "Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed)
                Guesses = Guesses -1
                print "_ _ _ _ _ _ _ _ _ _ _ _ \n"
                
        # When we finally run out of guesses
        if Guesses == 0:
            print "Sorry, you ran out of guesses. The word was " + str(secretWord) + "."

            
# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

""" Following function is commented out so that new function for secretWord(with user input) can be used"""
##secretWord = chooseWord(wordlist).lower()
word = raw_input("Choose the word: ")

# Function the guesses the secretWord
secretWord = word.lower()
hangman(secretWord)

