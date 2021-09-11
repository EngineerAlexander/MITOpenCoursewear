# Caesar Cipher: Pick integer and shift every letter by that integer to other letters in the alphabet. Be carefull with extremes
# let's map uppercase to upercase, lowercase to lowercase, and keep punctuation and spaces
# use message class with 2 subclasses: ciphertext, plaintext
# give message class methods that can be used to encrypt or decrypt message
# paintext class has methods to encode a string with a specific shift value
# ciphertext contains a method used to decode the string

import os

def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    #print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    #print("  ", len(wordlist), "words loaded.")
    inFile.close()
    return wordlist

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

def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        assert isinstance(text, str), 'Given input is not a string'
        
        self.message_text = text
        
        dir_path = os.path.dirname(os.path.realpath(__file__))
        file_name = '\\' + WORDLIST_FILENAME
        file_path = dir_path + file_name
        words_list = load_words(file_path)
        self.valid_words = []
        split_message_text = text.split(' ')
        for word in split_message_text:
            if is_word(words_list, word):
                self.valid_words.append(word)
        

    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words

    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26 [even though any integer will work]

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''

        # Uppercase shifts
        lower_bound = 'A'
        higher_bound = 'Z'

        lower_bound_dec = ord(lower_bound)
        higher_bound_dec = ord(higher_bound)

        list_nums = list(range(lower_bound_dec, higher_bound_dec + 1))
        list_chr = [chr(el) for el in list_nums]
        list_zero = [el - lower_bound_dec for el in list_nums]
        list_zero_shift = [el + shift for el in list_zero]

        list_zero_shift_fixed = []
        for el in list_zero_shift:
            while el < 0:
                el = el + list_zero[-1] + 1
            while el > list_zero[-1]:
                el = el - list_zero[-1] - 1
            list_zero_shift_fixed.append(el)

        ans_list = [el + lower_bound_dec for el in list_zero_shift_fixed]
        ans_list_chr = [chr(el) for el in ans_list]

        cipher_dict_1 = {}
        for i in range(len(list_chr)):
            cipher_dict_1[list_chr[i]] = ans_list_chr[i]
            
            
            
        # Lowercase shifts
        lower_bound = 'a'
        higher_bound = 'z'

        lower_bound_dec = ord(lower_bound)
        higher_bound_dec = ord(higher_bound)

        list_nums = list(range(lower_bound_dec, higher_bound_dec + 1))
        list_chr = [chr(el) for el in list_nums]
        list_zero = [el - lower_bound_dec for el in list_nums]
        list_zero_shift = [el + shift for el in list_zero]

        list_zero_shift_fixed = []
        for el in list_zero_shift:
            while el < 0:
                el = el + list_zero[-1] + 1
            while el > list_zero[-1]:
                el = el - list_zero[-1] - 1
            list_zero_shift_fixed.append(el)

        ans_list = [el + lower_bound_dec for el in list_zero_shift_fixed]
        ans_list_chr = [chr(el) for el in ans_list]

        cipher_dict_2 = {}
        for i in range(len(list_chr)):
            cipher_dict_2[list_chr[i]] = ans_list_chr[i]
            
        cipher_dict_1.update(cipher_dict_2)
        
        return cipher_dict_1

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26 [even though any integer will work]

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        assert isinstance(shift, int), 'Given shift is not an integer'
        
        shift_dict = self.build_shift_dict(shift)
        
        ignore_string = " !@#$%^&*()-_+={}[]|\:;'<>?,./\""
        
        new_message = ""
        for el in self.message_text:
            if el not in ignore_string:
                new_letter = shift_dict[el]
                new_message += new_letter
            else:
                new_message += el
        
        return new_message

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
            self.encryption_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        '''
        assert isinstance(text, str), 'Message is not a string'
        assert isinstance(shift, int), 'Shift is not an integer'
        
        super().__init__(text)
        
        self.shift = shift
        self.encryption_dict = super().build_shift_dict(shift)
        self.message_text_encrypted = super().apply_shift(shift)

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift

    def get_encryption_dict(self):
        '''
        Used to safely access a copy self.encryption_dict outside of the class
        
        Returns: a COPY of self.encryption_dict
        '''
        return self.encryption_dict

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift.        
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        self.shift = shift
        
        self.encryption_dict = super().build_shift_dict(shift)
        self.message_text_encrypted = super().apply_shift(shift)

class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        super().__init__(text)

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are equally good such that they all create 
        the maximum number of valid words, you may choose any of those shifts 
        (and their corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        dir_path = os.path.dirname(os.path.realpath(__file__))
        file_name = '\\' + WORDLIST_FILENAME
        file_path = dir_path + file_name
        words_list = load_words(file_path)
        
        actual_words = []
        for i in range(27):
            actual_words.append(0)
            new = super().apply_shift(i)
            newsplit = new.split(' ')
            for word in newsplit:
                if is_word(words_list, word):
                    actual_words[i] +=1
                    
        shift_index_max = max(range(len(actual_words)), key=actual_words.__getitem__)
        
        decrypt_message = super().apply_shift(shift_index_max)
        
        return (shift_index_max, decrypt_message)

if __name__ == '__main__':
    # Test cases for Message class
    print('Input: Hello there boys and girls!' )
    print('Expected Output: Hello there boys and girls! [\'Hello\' \'there\' \'boys\' \'and\' \'girls!\']' )
    message = Message('Hello there boys and girls!')
    print('Actual Output: ', message.get_message_text(), message.get_valid_words())

    print('Input: Are!' )
    print('Expected Output: {A:B r:s e:f ... all shifted by one ... Z:A z:a ...}' )
    message1 = Message('Are!')
    dict1 = message1.build_shift_dict(1)
    print('Actual Output: ', dict1)
    
    print('Input: Are!' )
    print('Expected Output: Bsf!' )
    message2 = Message('Are!')
    message2_enc = message2.apply_shift(1)
    print('Actual Output: ', message2_enc)
    
    # Test cases for PlaintextMessage class
    print('Input: Boyz!' )
    print('Expected Output: Boyz! []' )
    print('3 {A:D r:u e:h ... all shifted by one ... Z:C z:c ...} Erbc')
    message3 = PlaintextMessage('Boyz!', 3)
    print('Actual Output: ', message3.get_message_text(), message3.get_valid_words())
    print(message3.get_shift(), message3.get_encryption_dict(), message3.get_message_text_encrypted())
    
    message3.change_shift(2)
    print('Expected Output: Dqab!')
    print('Actual Output: ', message3.get_message_text_encrypted())
    
    # Test cases for CiphertextMessage
    
    print('Expected Output: (0, \'Is that the sky?\')')
    message4 = CiphertextMessage('Is that the sky?')
    print('Actual Output: ', message3.get_message_text_encrypted())
    
    print('Expected Output: (16, \'Is that the sky?\')')
    message5 = PlaintextMessage('Is that the sky?', 10)
    message5_dec = CiphertextMessage(message5.get_message_text_encrypted())
    print('Actual Output: ', message5_dec.decrypt_message())

    #TODO: best shift value and unencrypted story 
    
    pass #delete this line and replace with your code here
