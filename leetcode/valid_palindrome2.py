def check_palindrome(i, j, s):
    while i < j:
        if s[i] == s[j]:
            i += 1
            j -= 1
        else:
            return False
    return True


class Solution:
    def validPalindrome(self, s: str) -> bool:

        i = 0
        j = len(s) - 1

        # Go Greedy

        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return check_palindrome(i + 1, j, s) or check_palindrome(i, j - 1, s)

        return True