class Solution:

  def maxValue(self, nums: list[int]) -> list[int]:
    n = len(nums)

    # Calculate prefix maximums
    pref_max = [0] * n
    pref_max[0] = nums[0]
    for i in range(1, n):
      pref_max[i] = max(pref_max[i - 1], nums[i])

    # Calculate suffix minimums
    suff_min = [0] * n
    suff_min[-1] = nums[-1]
    for i in range(n - 2, -1, -1):
      suff_min[i] = min(suff_min[i + 1], nums[i])

    # Identify component boundaries and compute max for each component
    ans = [0] * n
    l = 0

    while l < n:
      r = l
      cur_max = nums[l]

      # Expand component until pref_max[r] <= suff_min[r + 1]
      while r < n - 1 and pref_max[r] > suff_min[r + 1]:
        r += 1
        cur_max = max(cur_max, nums[r])

      cur_max = max(cur_max, nums[r])

      # Assign max value to all indices within the connected component
      for i in range(l, r + 1):
        ans[i] = cur_max

      l = r + 1

    return ans