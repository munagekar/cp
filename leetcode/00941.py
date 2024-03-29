class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:

        l = len(arr)
        if l < 3:
            return False

        i = 0

        while i + 1 < l and arr[i] < arr[i + 1]:
            i += 1

        if i == 0 or i == l - 1:
            return False

        while i + 1 < l and arr[i] > arr[i + 1]:
            i += 1

        if i == l - 1:
            return True

        return False