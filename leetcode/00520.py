class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word.islower() or word.isupper() or word.istitle()


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return re.match("^[A-Z]?[a-z]*$", word) or re.match("^[A-Z]+$", word)
