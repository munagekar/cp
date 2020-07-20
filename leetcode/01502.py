class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr = sorted(arr)
        diff = arr[1]-arr[0]
        return all(x-y==diff for x,y in zip(arr[1:],arr[0:]))


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        s = set(arr)
        maxi = max(arr)
        mini = min(arr)
        d = (maxi - mini) / (len(arr) - 1)

        if not d.is_integer():
            return False

        if d == 0:
            return len(s) == 1

        return all(num in s for num in range(mini, maxi, int(d)))
