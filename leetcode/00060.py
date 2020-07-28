from math import factorial


def solve(choices_rem, ans, k):
    # print(choices_rem,ans,k)
    if not choices_rem:
        return ans
    opts = factorial(len(choices_rem) - 1)
    choose = max(k - 1, 0) // opts
    ans += str(choices_rem[choose])
    choices_rem = choices_rem[:choose] + choices_rem[choose + 1:]
    return solve(choices_rem, ans, k - choose * opts)


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        return solve(list(range(1, n + 1)), "", k)
