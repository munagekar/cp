class Solution:
    def findSecretWord(self, wordlist, master):
        for i in range(10):
            guess = random.choice(wordlist)
            x = master.guess(guess)
            wordlist = [w for w in wordlist if sum(i == j for i, j in zip(guess, w)) == x]