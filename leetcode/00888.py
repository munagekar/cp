class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        sumA = sum(A)
        sumB = sum(B)

        diff = (sumA - sumB) // 2

        B = set(B)

        for a in A:
            if a - diff in B:
                return [a, a - diff]