class Solution:
    def maximumJumps(self, nums: list[int], target: int) -> int:
        n = len(nums)
        # dp[i] stores the maximum number of jumps to reach index i from index 0
        dp = [-1] * n
        dp[0] = 0  # Starting point
        
        for j in range(1, n):
            for i in range(j):
                # If index i is reachable and the jump condition is satisfied
                if dp[i] != -1 and -target <= nums[j] - nums[i] <= target:
                    dp[j] = max(dp[j], dp[i] + 1)
                    
        return dp[n - 1]