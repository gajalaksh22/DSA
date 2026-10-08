class Solution:
    def sortColors(self, nums: list[int]) -> None:
        zero_count = 0
        one_count = 0
        two_count = 0
 
        # Count how many times each allowed value appears.
        for value in nums:
            # Increase the counter that matches the current value.
            if value == 0:
                zero_count += 1
            elif value == 1:
                one_count += 1
            else:
                two_count += 1
 
        index = 0
 
        # Write all zeroes first.
        for _ in range(zero_count):
            nums[index] = 0
            index += 1
 
        # Write all ones after the zeroes.
        for _ in range(one_count):
            nums[index] = 1
            index += 1
 
        # Write all twos at the end.
        for _ in range(two_count):
            nums[index] = 2
            index += 1
        return nums
        