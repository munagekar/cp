class Solution:
    def minInsertions(self, s: str) -> int:
        ins = 0

        st = []

        i = 0
        while i < len(s):
            if s[i] == "(":
                st.append("(")
                i += 1
                continue

            if i == len(s) - 1 or s[i + 1] != ")":
                ins += 1

                if st:
                    st.pop()
                else:
                    ins += 1
                i += 1
                continue

            if s[i + 1] == ")":
                if st:
                    st.pop()
                else:
                    ins += 1

                i += 2

        return len(st) * 2 + ins