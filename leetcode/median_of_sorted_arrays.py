# https://leetcode.com/problems/median-of-two-sorted-arrays/

from math import inf 

class Solution:
    def findMedianSortedArrays(self, arr1: List[int], arr2: List[int]) -> float:
        l1 = len(arr1)
        l2 = len(arr2)
        # First Array must be smaller or equal in size
        if l1 > l2:
            return self.findMedianSortedArrays(arr2, arr1)
        median_index = (l1 + l2 + 1) // 2
        is_even = True if (l1 + l2) % 2 == 0 else False

        low = 0
        high = l1

        while low <= high:
            # First array is partitioned into 2 parts
            # [:mid1], [:mid1] Pythonic indexing
            mid1 = (low + high) // 2
            # Array 2 is partitioned similarly
            mid2 = median_index - mid1

            arr1_left_last = -inf if mid1 == 0 else arr1[mid1 - 1]
            arr1_right_first = inf if mid1 == l1 else arr1[mid1]
            arr2_left_last = -inf if mid2 == 0 else arr2[mid2 - 1]
            arr2_right_first = inf if mid2 == l2 else arr2[mid2]

            if arr1_left_last <= arr2_right_first and arr1_right_first >= arr2_left_last:
                median1 = max(arr2_left_last, arr1_left_last)
                if not is_even:
                    return median1
                median2 = min(arr1_right_first, arr2_right_first)
                return (median1 + median2) /2

            if arr1_left_last > arr2_right_first:
                high = mid1 - 1
            else:
                low = mid1 + 1
        