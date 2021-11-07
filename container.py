import random
from cycle_swap import CycleSwap
from pointer_swap import PointerSwap
from number_swap import NumberSwap


# Generates random string.
def random_string() -> str:
    string = []
    for i in range(random.randint(10, 1000)):
        t = random.randint(1, 5)
        if t == 1:
            string.append(str(random.randint(0, 9)))
        else:
            string.append(chr(random.randint(97, 122)))
    return ''.join(string)


class Container:
    def __init__(self):
        self.storage = []

    # Fill container with data from file.
    def file_in(self, path: str) -> None:
        with open(file=path, mode='r') as file:
            while True:
                t = file.readline()
                if not t:
                    return
                if t == '1\n':
                    self.__add_file_cycle(file)
                if t == '2\n':
                    self.__add_file_number_swap(file)
                if t == '3\n':
                    self.__add_file_pointer(file)

    # Fills container with random objects.
    def random_in(self, amount: int) -> None:
        for i in range(amount):
            t = random.randint(1, 3)
            if t == 1:
                self.__add_random_cycle()
            if t == 2:
                self.__add_random_pointer()
            if t == 3:
                self.__add_random_number_swap()

    # Writes container data to file with specified path.
    def write_to(self, path: str) -> None:
        with open(file=path, mode='w') as file:
            k = str(self)
            file.write(k)

    # Sorts storage of container.
    def sort(self) -> None:
        self.storage.sort(key=lambda x: x.comparable)

    # Adding random CycleSwap to container.
    def __add_random_cycle(self) -> None:
        n = random.randint(0, 10000)
        self.storage.append(CycleSwap(decrypted=random_string(), n=n))

    # Adding random PointerSwap to container.
    def __add_random_pointer(self) -> None:
        table = {}
        alphabet = [chr(x) for x in list(range(48, 58)) + list(range(97, 123))]
        for i in list(range(48, 58)) + list(range(97, 123)):
            symbol = alphabet[random.randint(0, len(alphabet) - 1)]
            alphabet.remove(symbol)
            table[chr(i)] = symbol
        self.storage.append(PointerSwap(decrypted=random_string(), table=table))

    # Adding random NumberSwap to container.
    def __add_random_number_swap(self) -> None:
        table = {}
        alphabet = set()
        while len(alphabet) != 36:
            alphabet.add(random.randint(10, 1000))
        for i in list(range(48, 58)) + list(range(97, 123)):
            table[chr(i)] = alphabet.pop()
        self.storage.append(NumberSwap(decrypted=random_string(), table=table))

    # String representation of container.
    def __str__(self):
        string = ['Container:', f'Contains {len(self.storage)}.']
        for i in range(len(self.storage)):
            string.append(f'{i}: {str(self.storage[i])}')
        return '\n'.join(string)

    # Adding new CycleSwap to container from file.
    def __add_file_cycle(self, file):
        self.storage.append(CycleSwap(decrypted=file.readline().replace('\n', ''), n=int(file.readline())))

    # Adding new PointerSwap to container from file.
    def __add_file_pointer(self, file):
        decrypted = file.readline().replace('\n', '')
        table = {}
        for i in range(36):
            l, r = file.readline().split(' ')
            table[l] = r.replace('\n', '')
        self.storage.append(PointerSwap(decrypted=decrypted, table=table))

    # Adding new NumberSwap to container from file.
    def __add_file_number_swap(self, file):
        decrypted = file.readline().replace('\n', '')
        table = {}
        for i in range(36):
            l, r = file.readline().split(' ')
            table[l] = int(r)
        self.storage.append(NumberSwap(decrypted=decrypted, table=table))
