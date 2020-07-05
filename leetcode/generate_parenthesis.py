def solve(sol, base, open_par, close_par, limit):
    if close_par == limit:
        sol.append(base)
        return
    if close_par < open_par:
        solve(sol, base + ")", open_par, close_par + 1, limit)

    if open_par < limit:
        solve(sol, base + "(", open_par + 1, close_par, limit)


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        sol = []
        base = ""
        solve(sol, base, 0, 0, n)
        return sol