
""" Following are scripts for Finger exercises & problems in Week 06 - Lecture 12. """





# ----- Problem 03 -----
# ----------------------

import random 

class Hand(object):
    def __init__(self, n):
        '''
        Initialize a Hand.

        n: integer, the size of the hand.
        '''
        assert type(n) == int
        self.HAND_SIZE = n
        self.VOWELS = 'aeiou'
        self.CONSONANTS = 'bcdfghjklmnpqrstvwxyz'

        # Deal a new hand
        self.dealNewHand()

    def dealNewHand(self):
        '''
        Deals a new hand, and sets the hand attribute to the new hand.
        '''
        # Set self.hand to a new, empty dictionary
        self.hand = {}

        # Build the hand
        numVowels = self.HAND_SIZE / 3
    
        for i in range(numVowels):
            x = self.VOWELS[random.randrange(0,len(self.VOWELS))]
            self.hand[x] = self.hand.get(x, 0) + 1
        
        for i in range(numVowels, self.HAND_SIZE):    
            x = self.CONSONANTS[random.randrange(0,len(self.CONSONANTS))]
            self.hand[x] = self.hand.get(x, 0) + 1
            
    def setDummyHand(self, handString):
        '''
        Allows you to set a dummy hand. Useful for testing your implementation.

        handString: A string of letters you wish to be in the hand. Length of this
        string must be equal to self.HAND_SIZE.

        This method converts sets the hand attribute to a dictionary
        containing the letters of handString.
        '''
        assert len(handString) == self.HAND_SIZE, "Length of handString ({0}) must equal length of HAND_SIZE ({1})".format(len(handString), self.HAND_SIZE)
        self.hand = {}
        for char in handString:
            self.hand[char] = self.hand.get(char, 0) + 1


    def calculateLen(self):
        '''
        Calculate the length of the hand.
        '''
        ans = 0
        for k in self.hand:
            ans += self.hand[k]
        return ans
    
    def __str__(self):
        '''
        Display a string representation of the hand.
        '''
        output = ''
        hand_keys = self.hand.keys()
        hand_keys.sort()
        for letter in hand_keys:
            for j in range(self.hand[letter]):
                output += letter
        return output

    def update(self, word):
        """
        Does not assume that self.hand has all the letters in word.

        Updates the hand: if self.hand does have all the letters to make
        the word, modifies self.hand by using up the letters in the given word.

        Returns True if the word was able to be made with the letter in
        the hand; False otherwise.
        
        word: string
        returns: Boolean (if the word was or was not made)
        """
        Count = 0

        # Making a copy of string output
        CopyHand = self.__str__()

        # Making a copy of latest hand
        DummyHand = self.hand

        # If all the letters in the word are in the CopyHand (output)
        for letter in word:
            if letter in CopyHand:
                Count += 1

        # If Yes
        if Count == len(word):
            # For every letter in the word, reduce the value of key by 1 in the DummyHand
            for letter in word:
                if letter in self.hand.keys():
                    DummyHand[letter] -= 1
            # Updating main hand
            self.hand = DummyHand
            # Returnig Boolean as per specification
            return True
        # If No
        else:
            # Returnig Boolean as per specification
            return False



# Following are Sample Test provided in the Exercise     
##myHand = Hand(7)
##print myHand
##print myHand.calculateLen()
##
##myHand.setDummyHand('aulqqik')
##print myHand
##print myHand.calculateLen()
##
##print myHand.update('quail')
##print myHand





# ----- Problem 05 -----
# ----------------------

def genPrimes():

    """ Returns prime numbers."""
    
    Number = 3
    # Starting with 2
    List = [2]
    # First results must be 2
    next = 2
    yield next
    
    while True:
        Count = 0
        # For the Number, if Number can be divided item
        # on the list without a remainder then raise count
        for item in List:
            if Number % item != 0:
                Count += 1
            else:
                Count += 0
                
        #if that count and the length of the list is same
        # Return value and append list
        if Count == len(List):
            next = Number
            yield next
            List.append(Number)
            
        # Else, the list remains the same   
        elif Count != len(List):
            List = List
            
        # Trying only odd numbers
        Number += 2




 
