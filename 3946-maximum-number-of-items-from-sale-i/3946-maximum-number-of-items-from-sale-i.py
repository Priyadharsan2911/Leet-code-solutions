from typing import List


class Solution:

  def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
    n = len(items)

    # Precompute how many free copies activating item i grants
    free_from_first = [0] * n
    for i in range(n):
      fi = items[i][0]
      cnt = 0
      for j in range(n):
        if i != j and items[j][0] % fi == 0:
          cnt += 1
      free_from_first[i] = cnt

    dp = [0] * (budget + 1)

    for factor, price in items:
      if price > budget:
        continue

      # Find matching precomputed freebie count for this item
      # (Note: if duplicate [factor, price] pairs exist, each is a distinct item index)
      # Using enumerate over items directly avoids any lookup ambiguity:

    # Clean version iterating by index:
    dp = [0] * (budget + 1)
    for i, (_, price) in enumerate(items):
      if price > budget:
        continue

      bonus = 1 + free_from_first[i]

      # 1. First purchase of item i (0/1 step: go backwards)
      for b in range(budget, price - 1, -1):
        if dp[b - price] + bonus > dp[b]:
          dp[b] = dp[b - price] + bonus

      # 2. Additional copies of item i (unbounded step: go forwards)
      for b in range(price, budget + 1):
        if dp[b - price] + 1 > dp[b]:
          dp[b] = dp[b - price] + 1

    return max(dp)