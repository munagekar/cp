class Solution:
    def countBits(self, num: int) -> List[int]:
        ans = [0] * (num + 1)

        for i in range(1, num + 1):
            ans[i] = ans[i // 2] + (i & 1)

        return ans