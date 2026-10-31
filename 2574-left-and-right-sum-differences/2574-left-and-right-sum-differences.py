class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        total_sum = sum(nums)
        left_sum = 0
        ans = []
        for x in nums:
            right_sum = total_sum - left_sum - x
            ans.append(abs(left_sum - right_sum))
            left_sum += x
        return ans