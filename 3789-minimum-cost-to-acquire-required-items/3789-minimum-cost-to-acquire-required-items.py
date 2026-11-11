class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        common = min(need1, need2)
        rem1 = need1 - common
        rem2 = need2 - common
        
        # Cost to satisfy the overlapping requirement
        total_cost = common * min(costBoth, cost1 + cost2)
        
        # Cost to satisfy the remaining requirement (if any)
        if rem1 > 0:
            total_cost += rem1 * min(costBoth, cost1)
        elif rem2 > 0:
            total_cost += rem2 * min(costBoth, cost2)
            
        return total_cost