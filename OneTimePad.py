import random
from Cipher import Cipher

class OneTimePad(Cipher):
    def __init__(self):
        name = "One-Time Pad Cipher"
        explanation = "A bit, bit more complicated"
        additionalInputs = ["key"]
        Cipher.__init__(self,name=name,explanation=explanation)

    def encrypt(self,*args):
        if len(args) > 1:
            plaintext = args[0]
            keyword = args[1]
        elif len(args) == 1:
            plaintext = args[0]
            keyword = ''.join(random.choice(self.alphabet) for i in range(len(plaintext)))
        else:
            plaintext = input("Enter plaintext: ")
            keyword = input("Enter key (a random string of a certain length): ")
        ciphertext = list(plaintext)
        w=0
        for j in range(0,len(ciphertext)):
            char = plaintext[j]
            if char.lower() in self.alphabet:
                i = self.alphabet.index(char.lower())
                if w >= len(keyword):
                    w = 0
                i = i + self.alphabet.index(keyword[w].lower())
                w+=1
                if (i > 25):
                    i -= 26
                if ciphertext[j].isupper():
                    ciphertext[j] = self.alphabet[i].upper()
                else:
                    ciphertext[j] = self.alphabet[i]
        ciphertext = "".join(ciphertext)
        return ({"ciphertext":ciphertext,"keyword":keyword,"plaintext":plaintext})