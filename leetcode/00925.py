def reducer(s):
    l = len(s)
    p = 0
    ans = []
    while p < l:
        char = s[p]
        counter = 0
        while p < l and s[p] == char:
            counter += 1
            p += 1
        ans.append((char, counter))

    return ans


class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        r_name = reducer(name)
        r_typed = reducer(typed)

        print(r_name)
        print(r_typed)

        if len(r_name) != len(r_typed):
            return False

        return all(x <= y and a == b for ((a, x), (b, y)) in zip(r_name, r_typed))
