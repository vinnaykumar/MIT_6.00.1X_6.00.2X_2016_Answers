import string

### DO NOT MODIFY THIS FUNCTION ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
##    print 'Loading word list from file...'
    # inFile: file
    in_file = open(file_name, 'r', 0)
    # line: string
    line = in_file.readline()
    # word_list: list of strings
    word_list = line.split()
##    print '  ', len(word_list), 'words loaded.'
    in_file.close()
    return word_list

### DO NOT MODIFY THIS FUNCTION ###
def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

### DO NOT MODIFY THIS FUNCTION ###
def get_story_string():
    """
    Returns: a joke in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    ### DO NOT MODIFY THIS METHOD ###
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    ### DO NOT MODIFY THIS METHOD ###
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    ### DO NOT MODIFY THIS METHOD ###
    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]
        
    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        # Oroginal Lists
        a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        b = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

        # This part generates a list of all small letters shifted by "shift"(integer)
        catch01 = []
        for item in a:
            if a.index(item) + shift <= 25:
                NewIndex = a.index(item) + shift
                catch01.append(a[NewIndex])

            elif a.index(item) + shift > 25:
                NewIndex = a.index(item) + shift - 26
                catch01.append(a[NewIndex])
                
        # This part generates a list of all capital letters shifted by "shift"(integer)
        catch02 = []
        for item in b:
            if b.index(item) + shift <= 25:
                NewIndex = b.index(item) + shift
                catch02.append(b[NewIndex])

            elif b.index(item) + shift > 25:
                NewIndex = b.index(item) + shift - 26
                catch02.append(b[NewIndex])
                
        # Dictionaries created from original list and shifted list              
        dict01 = dict(zip(a, catch01))
        dict02 = dict(zip(b, catch02))

        # Dictionaries concatenated
        Finaldict = dict(dict01.items() + dict02.items())
        return Finaldict        
        

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        # Using pre-defined methods
        Refdict = Message.build_shift_dict(self, shift)
        Text = Message.get_message_text(self)

        Container = " "

        for letter in Text:
            # if letter is in keys, the letter is replaced by its value in the Refdict            
            if letter in Refdict.keys():
                Container += Refdict[letter]
            # if letter is not in keys, the same letter is given back 
            elif letter not in Refdict.keys():
                Container += letter

        return Container[1:]

        

class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encrypting_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        Hint: consider using the parent class constructor so less 
        code is repeated
        '''
        self.message_text = text
        self.shift = shift
        self.encrypting_dict = Message.build_shift_dict(self, self.shift)
        self.message_text_encrypted = Message.apply_shift(self, self.shift)
        

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift

    def get_encrypting_dict(self):
        '''
        Used to safely access a copy self.encrypting_dict outside of the class
        
        Returns: a COPY of self.encrypting_dict
        '''
        return self.encrypting_dict.copy()

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift (ie. self.encrypting_dict and 
        message_text_encrypted).
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        # Changing(Re-defining shift)
        self.shift = shift
        # Re-defining following attributes as per new shift defined in this method
        self.encrypting_dict = Message.build_shift_dict(self, shift)
        self.message_text_encrypted = Message.apply_shift(self, shift)


class CiphertextMessage(Message):
    
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are  equally good such that they all create 
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        
        # Shift
        shift = 0
        # Counter
        count = 0
        # This is for cheking the counter
        hold = 0
        # This will catch all the english words(strings)
        s = []
        # This will capture all the hits
        hitlist = []
        # This will capture all the shifts
        shiftlist = []
        
        while shift < 26:
            # This is very important. In every iteration,
            # the hits must start with a 0
            hits = 0
            # Splitting the word first
            Splitword = self.apply_shift(shift).split(' ')
            for word in Splitword:
                if is_word(self.valid_words, word) == True:
                    hits += 1
            # This identation is important.
            # This can not be inside the for loop
            hitlist.append(hits)
            shiftlist.append(shift)
            shift += 1

        # Basically making a dictionary from two lists
        # This dictionary will have {hits : shifft} structure
        Dict = dict(zip(hitlist, shiftlist))
        # Extracting the higest value in hitlist
        # This will give us the key that is the biggest number
        Maxhits = max(Dict.keys())
        # Now we use that key to extract the value of shift associated with it
        selshift = Dict[Maxhits]

        #Finally, returning a Tuple of selected shift, and decrypted text
        # Make a note, selshift is used to decrypt the text right here.
        return (selshift, self.apply_shift(selshift))
        

    

##Example test case (PlaintextMessage)
plaintext = PlaintextMessage('smoke remind kneel cream twist', 3)
print 'Expected Output: jgnnq'
print 'Actual Output:', plaintext.get_message_text_encrypted()
print " "
  
###Example test case (CiphertextMessage)
ciphertext = CiphertextMessage('qkmic pckglb ilccj apcyk rugqr')
print 'Expected Output:', (2, 'smoke remind kneel cream twist')
print 'Actual Output:', ciphertext.decrypt_message()





def decrypt_story():

    """
    This function uses an encrypted string and
    returns the encryption key and decrypted message in a Tuple.
    """

    # Getting the strins out of story.txt file provide by Edx
    Story = get_story_string()
    # Creating an object of CiphertextMessage to use that subclass
    Decrypt = CiphertextMessage(Story)
    # Accessing one the methods of CiphertextMessage and returning the
    # result
    return Decrypt.decrypt_message()


# Printing to Check decrypt_story()
##print " "
##print decrypt_story()
