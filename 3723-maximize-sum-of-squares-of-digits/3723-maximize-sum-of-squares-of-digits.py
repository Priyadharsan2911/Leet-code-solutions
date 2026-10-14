class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        # Check if it's even possible to form the sum with 'num' digits (max possible sum is num * 9)
        if sum > num * 9 or sum < 1:
            return ""
        
        res = []
        for i in range(num):
            # Take as much as possible for the current digit, up to 9, 
            # but leave enough capacity for the remaining positions if needed, 
            # or just greedily take min(9, sum).
            # Wait, since we want the *maximum number* when scores are equal,
            # putting larger digits at the *beginning* (left) is optimal.
            val = min(9, sum)
            res.append(str(val))
            sum -= val
            
        # If any sum is left over, we couldn't fit it into 'num' digits properly
        if sum > 0:
            return ""
            
        return "".join(res)