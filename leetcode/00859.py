class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False

        mismatch = 0
        char_reqd = None
        char_got = None

        second_cond = False

        d = collections.defaultdict(lambda: 0)

        for a, b in zip(A, B):

            d[a] += 1
            if d[a] == 2:
                second_cond = True
            if a != b:
                if mismatch == 0:
                    mismatch += 1
                    char_reqd = b
                    char_got = a
                elif mismatch == 1:
                    if a == char_reqd and char_got == b:
                        mismatch += 1
                        continue
                    else:
                        return False
                else:
                    return False

        if mismatch == 2:
            return True

        if mismatch == 1:
            return False

        return False or second_cond


class Solution2:
    def buddyStrings(self, A: str, B: str) -> bool:
        if A == B:
            if len(set(A)) != len(A):
                return True
            else:
                return False

        if len(A) != len(B):
            return False

        p = [[a, b] for a, b in zip(A, B) if a != b]
        if len(p) != 2:
            return False

        return False or p[0] == p[1][::-1]
