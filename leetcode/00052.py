class Solution:
    def totalNQueens(self, n: int) -> int:
        cols = set()
        diag_sum = set()
        diag_sub = set()
        count = 0

        def helper(row):
            nonlocal count

            if row == n:
                count += 1
                return

            for col in range(n):
                if col not in cols and col + row not in diag_sum and col - row not in diag_sub:
                    cols.add(col)
                    diag_sum.add(col + row)
                    diag_sub.add(col - row)
                    helper(row + 1)

                    cols.remove(col)
                    diag_sum.remove(col + row)
                    diag_sub.remove(col - row)

        helper(0)
        return count