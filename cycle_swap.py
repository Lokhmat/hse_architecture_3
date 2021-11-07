from cipher import Cipher


# Implementation of CycleSwap cipher. Derived from Cipher class.
class CycleSwap(Cipher):
    def __init__(self, decrypted: str, n: int):
        super().__init__(decrypted=decrypted)
        self.n = n
        self.encrypted = ''
        self.__generate_encrypted()

    # Generate encrypted string from decrypted and rule.
    def __generate_encrypted(self) -> None:
        temp = []
        for el in self.decrypted:
            if el.isdecimal():
                temp.append(chr((ord(el) - 48 + self.n) % 10 + 48))
            else:
                temp.append(chr((ord(el) - 97 + self.n) % 26 + 97))
        self.encrypted = ''.join(temp)

    # String representation of CycleSwap.
    def __str__(self) -> str:
        return f'CycleSwap:\nDecrypted:{self.decrypted}\nEncrypted:{self.encrypted}\n' \
               f'N={self.n}\nComparable:{self.comparable}'
