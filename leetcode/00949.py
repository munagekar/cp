class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:

        def is_valid2(x):
            return is_valid(*x)

        def is_valid(x1, x2, x3, x4):
            if x1 * 10 + x2 < 24 and x3 * 10 + x4 < 60:
                return True

        def value2(x):
            return value(*x)

        def value(x1, x2, x3, x4):
            return 1000 * x1 + 100 * x2 + 10 * x3 + x4

        def to_string2(x):
            return to_string(*x)

        def to_string(x1, x2, x3, x4):
            return f"{x1 * 10 + x2:02d}:{x3 * 10 + x4:02d}"

        try:
            combination = max(filter(is_valid2, itertools.permutations(A, 4)), key=value2)
            return to_string2(combination)
        except:
            return ""