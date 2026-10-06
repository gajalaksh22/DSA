class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        def count_array(nums,arr):
            arrays = 1
            elements = 0
            for i in range(len(nums)):
                if elements + nums[i] <= arr:
                    elements += nums[i]
                else:
                    arrays += 1
                    elements = nums[i]
            return arrays
        n = len(nums)
        if k > n:
            return -1
        low = max(nums)
        high = sum(nums)
        while low <= high:
            mid = (low + high) // 2
            arrays = count_array(nums,mid)
            if arrays > k:
                low = mid + 1
            else:
                high = mid - 1
        return low
