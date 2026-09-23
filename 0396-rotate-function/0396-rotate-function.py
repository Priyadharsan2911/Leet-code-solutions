class Solution:
    def maxRotateFunction(self, nums: list[int]) -> int:
        n = len(nums)
        total_sum = sum(nums)
        
        # Base state F(0)
        current_f = sum(i * val for i, val in enumerate(nums))
        max_f = current_f
        
        # O(1) transitions to compute F(1) through F(n-1)
        for k in range(1, n):
            current_f += total_sum - n * nums[n - k]
            max_f = max(max_f, current_f)
            
        return max_f