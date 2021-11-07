from cipher import Cipher


# Implementation of NumberSwap cipher. Derived from Cipher class.
class NumberSwap(Cipher):
    def __init__(self, decrypted: str, table: dict):
        super().__init__(decrypted=decrypted)
        self.table = table
        self.encrypted = ''
        self.generate_encrypted()

    # Generate encrypted string from decrypted and rule.
    def generate_encrypted(self) -> None:
        temp = []
        for el in self.decrypted:
            temp.append(str(self.table[el]))
        self.encrypted = ' '.join(temp)

    # String representation of NumberSwap.
    def __str__(self) -> str:
        string = [
            'NumberSwap:',
            f'Decrypted:{self.decrypted}',
            f'Encrypted:{self.encrypted}',
        ]
        for i in self.table:
            string.append(f'{i} {self.table[i]}')
        string.append(f'Comparable: {self.comparable}')
        return '\n'.join(string)
