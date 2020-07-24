import bisect


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        right = bisect.bisect_left(arr, x)
        if right == 0:
            left = 0
            right = 1
        else:
            left = right - 1

        res = []
        for _ in range(k):
            if left >= 0 and (right >= len(arr) or (x - arr[left] <= arr[right] - x)):
                res.append(arr[left])
                left -= 1
            elif right < len(arr):
                res.append(arr[right])
                right += 1

        return sorted(res)