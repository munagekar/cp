class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        s = S
        s = s.replace("-", "")
        s = s.upper()
        fg = len(s) % K or K

        ans = s[:fg]

        l = fg + K
        while l <= len(s):
            ans += "-"
            ans += s[l - K:l]
            l += K
        return ans