from string import ascii_lowercase


class TrieNode():

    def __init__(self):
        self.char_map = {}
        self.word = False


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self.root
        for c in word:
            t = node.char_map.get(c)
            if not t:
                t = TrieNode()
                node.char_map[c] = t
            node = t

        node.word = True

    def search(self, word: str) -> bool:
        t = self.search2(word, self.root, 0)
        print(t)
        return t

    def search2(self, word: str, node, index) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        if not node:
            return False
        if index == len(word):
            return node.word

        char = word[index]
        if char != ".":
            return self.search2(word, node.char_map.get(char), index + 1)

        for n in node.char_map.values():
            if self.search2(word, n, index + 1):
                return True

        return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)