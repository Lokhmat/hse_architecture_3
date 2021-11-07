# Implementation of base class Cipher.
class Cipher:
    def __init__(self, decrypted: str):
        self.decrypted = decrypted
        self.comparable = 0
        self.__set_comparable()

    # Set comparable as a variable for faster sorting.
    def __set_comparable(self):
        for el in self.decrypted:
            self.comparable += ord(el)
        self.comparable /= float(len(self.decrypted))
