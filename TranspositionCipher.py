import random
from Cipher import Cipher

class TranspositionCipher(Cipher):
    def __init__(self):
        name = "Vigenere Cipher"
        explanation = "A bit more simple"
        additionalInputs = ["reordering"]
        Cipher.__init__(self,name=name,explanation=explanation)

    def encrypt(self,*args):
        if len(args) > 1:
            plaintext = args[0]
            reordering = args[1]
        elif len(args) == 1:
            plaintext = args[0]
            randomordering = list(range(0,len(plaintext)-1))
            reordering = []
            while randomordering:
                next = random.choice(randomordering)
                reordering.append(next)
                randomordering.remove(next)
        else:
            plaintext = input("Enter plaintext: ")
            keyword = input("Enter reordering (a list): ")
        ciphertext = list(plaintext)
        for i in range(0,len(reordering)):
            j = reordering[i]
            ciphertext[i] = plaintext[j]
        ciphertext = "".join(ciphertext)
        return ({"ciphertext":ciphertext,"reordering":reordering,"plaintext":plaintext})