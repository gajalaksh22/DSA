class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        merged: List[int] = []
 
        for value in nums1:
            merged.append(value)
 
        for value in nums2:
            merged.append(value)
 
        # Sorting creates the final order needed for median calculation.
        merged.sort()
 
        # This is the total number of values after both arrays are combined.
        total: int = len(merged)
 
        # If total is odd, there is one exact middle element.
        if total % 2 == 1:
            return float(merged[total // 2])
        else:
            # If total is even, the median is the average
            # of the two middle elements.
            return (merged[total // 2 - 1] + merged[total // 2]) / 2.0
 
 
        