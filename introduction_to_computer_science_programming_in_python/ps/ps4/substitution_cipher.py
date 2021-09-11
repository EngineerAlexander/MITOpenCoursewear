import string
import os
import permutations_of_string

### HELPER CODE ###
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


### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

# you may find these constants helpful
VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'

class SubMessage(object):
    def __init__(self, text):
        '''
        Initializes a SubMessage object
                
        text (string): the message's text

        A SubMessage object has two attributes:
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
                
    def build_transpose_dict(self, vowels_permutation):
        '''
        vowels_permutation (string): a string containing a permutation of vowels (a, e, i, o, u)
        
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to an
        uppercase and lowercase letter, respectively. Vowels are shuffled 
        according to vowels_permutation. The first letter in vowels_permutation 
        corresponds to a, the second to e, and so on in the order a, e, i, o, u.
        The consonants remain the same. The dictionary should have 52 
        keys of all the uppercase letters and all the lowercase letters.

        Example: When input "eaiuo":
        Mapping is a->e, e->a, i->i, o->u, u->o
        and "Hello World!" maps to "Hallu Wurld!"

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        assert isinstance(vowels_permutation, str), 'Input is not a string'
        assert len(vowels_permutation)==5, 'Input is not of len(english_vowels)'
        
        mapping_dict = {}
        
        vowels_permutation.lower()
        for i in range(5):
            mapping_dict[VOWELS_LOWER[i]] = vowels_permutation[i]
            
        vowels_permutation.upper()
        for i in range(5):
            mapping_dict[VOWELS_UPPER[i]] = vowels_permutation[i]
            
        for el in CONSONANTS_LOWER:
            mapping_dict[el] = el
        
        for el in CONSONANTS_UPPER:
            mapping_dict[el] = el
        
        return mapping_dict
    
    def apply_transpose(self, transpose_dict):
        '''
        transpose_dict (dict): a transpose dictionary
        
        Returns: an encrypted version of the message text, based 
        on the dictionary
        '''
        new = ""
        for el in self.message_text:
            if el in transpose_dict.keys():
                new += transpose_dict[el]
            else:
                new += el
            
        return new
        
class EncryptedSubMessage(SubMessage):
    def __init__(self, text):
        '''
        Initializes an EncryptedSubMessage object

        text (string): the encrypted message text

        An EncryptedSubMessage object inherits from SubMessage and has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        super().__init__(text)

    def decrypt_message(self):
        '''
        Attempt to decrypt the encrypted message 
        
        Idea is to go through each permutation of the vowels and test it
        on the encrypted message. For each permutation, check how many
        words in the decrypted text are valid English words, and return
        the decrypted message with the most English words.
        
        If no good permutations are found (i.e. no permutations result in 
        at least 1 valid word), return the original string. If there are
        multiple permutations that yield the maximum number of words, return any
        one of them.

        Returns: a tuple of the number of english words and the best decrypted message    
        
        Hint: use your function from Part 4A
        '''
        dir_path = os.path.dirname(os.path.realpath(__file__))
        file_name = '\\' + WORDLIST_FILENAME
        file_path = dir_path + file_name
        words_list = load_words(file_path)
        
        permutations_words = []
        permutations_vowels_lower = permutations_of_string.permutations(VOWELS_LOWER)
        for i in range(len(permutations_vowels_lower)):
            current_dict = super().build_transpose_dict(permutations_vowels_lower[i])
            new_text = super().apply_transpose(current_dict)
            new_text_split = new_text.split(' ')
            
            permutations_words.append(0)
            for word in new_text_split:
                if is_word(words_list, word):
                    permutations_words[i] += 1
                    
        perm_index_max = max(range(len(permutations_words)), key=permutations_words.__getitem__)
        
        if permutations_words[perm_index_max] == 0:
            return (len(self.valid_words), self.message_text)
        
        best_dict = super().build_transpose_dict(permutations_vowels_lower[perm_index_max])
        best_text = super().apply_transpose(best_dict)
        
        
        return (permutations_words[perm_index_max], best_text)
    

if __name__ == '__main__':

    # Test cases for class note could do this more effeciently with function
    message = SubMessage("Hello World!")
    permutation = "eaiuo"
    enc_dict = message.build_transpose_dict(permutation)
    print("Original message:", message.get_message_text(), "Permutation:", permutation)
    print("Expected encryption:", "Hallu Wurld!")
    print("Actual encryption:", message.apply_transpose(enc_dict))
    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    print("Decrypted message:", enc_message.decrypt_message(), "\n")
    
    message2 = SubMessage("The world is your oyster?")
    permutation = "eaiuo"
    enc_dict2 = message2.build_transpose_dict(permutation)
    print("Original message:", message2.get_message_text(), "Permutation:", permutation)
    print("Expected encryption:", "Tha wurld is yuor uystar?")
    print("Actual encryption:", message2.apply_transpose(enc_dict2))
    enc_message2 = EncryptedSubMessage(message2.apply_transpose(enc_dict2))
    print("Decrypted message:", enc_message2.decrypt_message())
    print("This is not the original string but is still valid cause it maximizes english words\n")
    
    message3 = SubMessage("jibaoiuhqocva asduhougasdfgf akcvxoziuv?")
    permutation = "iaoeu"
    enc_dict3 = message3.build_transpose_dict(permutation)
    print("Original message:", message3.get_message_text(), "Permutation:", permutation)
    print("Actual encryption:", message3.apply_transpose(enc_dict3))
    enc_message3 = EncryptedSubMessage(message3.apply_transpose(enc_dict3))
    print("Decrypted message:", enc_message3.decrypt_message())
    print("This had no decryptions that maximized words so we returned the original string of the encrypted message\n")
    
