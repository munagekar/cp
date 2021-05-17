class Solution:
    def binaryGap(self, n: int) -> int:

        memory = None

        ans = 0
        idx = 0
        while n != 0:
            if n % 2:
                if memory is None:
                    memory = idx
                else:
                    ans = max(ans, idx - memory)
                    memory = idx
            n //= 2
            idx += 1

        return ans
