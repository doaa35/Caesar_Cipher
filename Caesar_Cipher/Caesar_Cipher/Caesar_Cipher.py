class CaesarCipher:

    default_key={"a": "d", "b": "e", "c": "f", "d": "g", "e": "h", "f": "i", "g": "j",
                    "h": "k","i": "l", "j": "m", "k": "n", "l": "o", "m": "p", "n": "q", "o":
                    "r", "p": "s","q": "t", "r": "u", "s": "v", "t": "w", "u": "x", "v": "y",
                    "w": "z", "x": "a","y": "b", "z": "c", " ":" "}
       
    def __init__(self, key:dict=None)->str:
        
        if key is None:
            key = self.default_key
            
        self.key = key

        self.antikey = {val:k for k,val in key.items()}
        

    # Method that takes the the message you want to encrypt and
    # returns it as encrypted    
    def encrypt_string(self,message:str):

        encrypted = ''
        
        self.check_input(message)

        lower_message = message.lower()
        
        #getting char's cipher from key and concat it with encrypted variable 
        for ch in lower_message:
            encrypted+= (self.key[ch])

        return encrypted


    #  Method that takes an encrypted string and tries to decrypt it    
    def decrypt_string(self,message:str)->str:

        decrypted = ''
        
        # no need to lower the message, encrypted is in lower case already
        
        #getting char's decrypted value from antikey
        for ch in message:
            decrypted+= (self.antikey[ch])

        return decrypted
 #check_input method is decorated with @staticmethod because it does not operate on
 # any instance attributes (self) or require access to instance-specific data. 
 # It's a utility method that simply checks whether a given string contains only alphabets and spaces.
    
    @staticmethod
    def check_input(message:str)->str:

        # The all() function returns True if all items in an iterable are true, otherwise it returns False.
        # If the iterable object is empty, the all() function also returns True.

        if not all(char.isalpha() or char.isspace() for char in message):
            raise ValueError("Input text must contain only alphabets and spaces.")
        


def get_cipher(string:str, key=None, encrypt=True):

    if encrypt:
        obj=CaesarCipher(key=key)
        obj.check_input(string)
        return obj.encrypt_string(message=string)
    else:
        obj=CaesarCipher(key=key)
        return obj.decrypt_string(message=string)
      
