from cipher import Cipher


# Implementation of PointerSwap cipher. Derived from Cipher class.
class PointerSwap(Cipher):
    def __init__(self, decrypted: str, table: dict):
        super().__init__(decrypted=decrypted)
        self.table = table
        self.encrypted = ''
        self.__generate_encrypted()

    # Generate encrypted string from decrypted and rule.
    def __generate_encrypted(self) -> None:
        temp = []
        for el in self.decrypted:
            temp.append(self.table[el])
        self.encrypted = ''.join(temp)

    # String representation of PointerSwap.
    def __str__(self) -> str:
        string = [
            'PointerSwap:',
            f'Decrypted:{self.decrypted}',
            f'Encrypted:{self.encrypted}',
        ]
        for i in self.table:
            string.append(f'{i} {self.table[i]}')
        string.append(f'Comparable: {self.comparable}')
        return '\n'.join(string)
