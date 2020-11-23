class Solution:
    def shortestPalindrome(self, s: str) -> str:
        r = s[::-1]

        for i in range(len(s) + 1):
            if s.startswith(r[i:]):
                return r[:i] + s


def prefix_arr(t):
    l = len(t)

    arr = [0] * l
    j = 0
    i = 1
    while i < l:
        if t[i] == t[j]:
            arr[i] = j + 1
            i += 1
            j += 1
        else:
            if j == 0:
                i += 1
            else:
                j = arr[j - 1]
    return arr


class Solution2:
    def shortestPalindrome(self, s: str) -> str:
        r = s[::-1]

        t = s + "#" + r
        arr = prefix_arr(t)
        match = arr[-1]
        ans = r[:-match] + s

        return ans