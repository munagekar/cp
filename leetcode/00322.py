class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        d = {0: 0}

        def fn(x):
            if x < 0:
                return math.inf

            if x in d:
                return d[x]

            v = min(1 + fn(x - c) for c in coins)
            d[x] = v
            return v

        x = fn(amount)
        if x < math.inf:
            return x
        else:
            return -1