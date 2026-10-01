class Solution:
    def maxValue(self, nums: list[int]) -> list[int]:
        n = len(nums)
        if n == 1:
            return [nums[0]]

        # Prefix maximums from left to right
        pref_max = [0] * n
        pref_max[0] = nums[0]
        for i in range(1, n):
            pref_max[i] = max(pref_max[i - 1], nums[i])

        # Suffix minimums from right to left
        suff_min = [0] * n
        suff_min[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            suff_min[i] = min(suff_min[i + 1], nums[i])

        ans = [0] * n
        l = 0

        # Divide into connected components where jump boundaries occur
        # when pref_max[r] <= suff_min[r + 1]
        while l < n:
            r = l
            cur_max = nums[l]
            while r < n - 1 and pref_max[r] > suff_min[r + 1]:
                r += 1
                cur_max = max(cur_max, nums[r])

            cur_max = max(cur_max, nums[r])

            # All indices in the same component can reach cur_max
            for i in range(l, r + 1):
                ans[i] = cur_max

            l = r + 1

        return ans