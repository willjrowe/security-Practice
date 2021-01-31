import random
from Cipher import Cipher

class CaesarCipher(Cipher):
    def __init__(self):
        name = "Caesar Cipher"
        explanation = "Simple letter rotation by k"
        additionalInputs = ["k"]
        Cipher.__init__(self,name=name,explanation=explanation)

    def encrypt(self,*args):
        if len(args) > 1:
            plaintext = args[0]
            k = args[1]
        elif len(args) == 1:
            plaintext = args[0]
            k = random.randint(1,24)
        else:
            plaintext = input("Enter plaintext: ")
            k = int(input("Enter k (an int): "))
        ciphertext = list(plaintext)
        for j in range(0,len(ciphertext)):
            char = plaintext[j]
            if char.lower() in self.alphabet:
                i = self.alphabet.index(char.lower())
                i = i + k
                if (i > 25):
                    i -= 26
                if ciphertext[j].isupper():
                    ciphertext[j] = self.alphabet[i].upper()
                else:
                    ciphertext[j] = self.alphabet[i]
        ciphertext = "".join(ciphertext)
        return ({"ciphertext":ciphertext,"k":k,"plaintext":plaintext})

    def decrypt(self,*args):
        if len(args) > 1:
            ciphertext = args[0]
            k = args[1]
        else:
            ciphertext = input("Enter ciphertext: ")
            k = int(input("Enter k (an int): "))
        plaintext = list(ciphertext)
        for j in range(0,len(plaintext)):
            char = ciphertext[j]
            if char.lower() in self.alphabet:
                i = self.alphabet.index(char.lower())
                i = i - k
                if (i < 0):
                    i += 26
                if plaintext[j].isupper():
                    plaintext[j] = self.alphabet[i].upper()
                else:
                    plaintext[j] = self.alphabet[i]
        plaintext = "".join(plaintext)
        print(ciphertext + " - cipheretext")
        print(plaintext + " - plaintext")