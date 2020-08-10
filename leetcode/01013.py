class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        total = sum(A)
        t3, rem = divmod(total, 3)
        if rem:
            return False

        runner = 0
        parts = 0
        for i, x in enumerate(A):
            runner += x
            if runner == t3:
                parts += 1
                runner = 0
                if parts == 2 and i != len(A) - 1:
                    return True
        return False