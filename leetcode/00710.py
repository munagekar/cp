class Solution:

    def __init__(self, n: int, blacklist: List[int]):
        self.b = set(blacklist)
        self.m = {}
        self.length = n - len(self.b)
        self.r = [x for x in self.b if x < self.length]

        j = 0
        for i in range(self.length, n):
            if i not in self.b:
                self.m[self.r[j]] = i
                j += 1

        print(self.m)

    def pick(self) -> int:
        v = random.randrange(self.length)
        return v if v not in self.b else self.m[v]

# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()