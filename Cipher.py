import random
from constants import testPlaintext

class Cipher:
    def __init__(self, name, explanation, **kwargs):
        self.name = name
        self.explanation = explanation
        self.hasAdditionalInputs = False
        self.alphabet = alphabet = ["a", "b", "c", "d", "e", "f", "g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        if "additionalInputs" in kwargs:
            self.hasAdditionalInputs = True
            self.additionalInputs = kwargs.get("additionalInputs")
            for val in self.additionalInputs:
                setattr(self, val, None)
        self.promptInput()

    def explain(self):
        print(self.name + " - " + self.explanation)

    def example(self):
        plaintext = random.choice(testPlaintext)
        encrypted = self.encrypt(plaintext)
        print(encrypted)

    def practiceDecrypt(self):
        plaintext = random.choice(testPlaintext)
        encrypted = self.encrypt(plaintext)
        ciphertext = encrypted["ciphertext"]
        print("Try to guess the exact phrase: ")
        print(ciphertext + " - ciphertext")
        guess = ""
        while (guess != plaintext):
            guess = input("What do you think the phrase is?")
            if (guess != plaintext):
                print("Not quite. Guess again.")
                print(ciphertext + " - ciphertext")
            if (guess == "giveup"):
                break
        print(encrypted)

    def encrypt(self):
        pass

    def decrypt(self):
        pass

    def printProperties(self):
        print(self.__dict__)

    def promptInput(self):
        if self.hasAdditionalInputs:
            for val in self.additionalInputs:
                newVal = input("Enter " + val + ": ")
                setattr(self, val, newVal)



    


