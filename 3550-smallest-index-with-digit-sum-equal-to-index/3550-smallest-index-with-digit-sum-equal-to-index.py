class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            # Calculate digit sum of nums[i]
            digit_sum = sum(int(digit) for digit in str(num))
            
            # Check if digit sum equals index i
            if digit_sum == i:
                return i
                
        return -1