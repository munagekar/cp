class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        random.shuffle(nums)

        k = len(nums) - k

        def partition(arr, l, h):

            t = arr[l]
            i = l
            for j in range(l, h + 1):
                if arr[j] <= t:
                    arr[j], arr[i] = arr[i], arr[j]
                    i += 1
            arr[i - 1], arr[l] = arr[l], arr[i - 1]
            return i - 1

        l = 0
        h = len(nums) - 1

        while True:
            i = partition(nums, l, h)

            if i == k:
                return nums[i]

            if i < k:
                l = i + 1

            else:
                h = i - 1