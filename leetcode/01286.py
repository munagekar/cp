class CombinationIterator:

    def __init__(self, characters: str, l: int):
        self.characters = characters
        self.pointers = list(range(l))
        self.n = len(characters)
        self.l = l
        self.last = "".join([self.characters[i] for i in range(self.n - l, self.n)])
        self.output = None

    def next(self) -> str:
        output = "".join([self.characters[i] for i in self.pointers])
        self.output = output
        for i in range(self.l - 1, -1, -1):
            if i == self.l - 1 and self.pointers[i] != self.n - 1:
                self.pointers[i] += 1
                break

            elif i < self.l - 1 and self.pointers[i] + 1 < self.pointers[i + 1]:
                self.pointers[i] += 1
                for j in range(i + 1, self.l):
                    self.pointers[j] = self.pointers[j - 1] + 1
                break

        return output

    def hasNext(self) -> bool:
        return not self.output == self.last