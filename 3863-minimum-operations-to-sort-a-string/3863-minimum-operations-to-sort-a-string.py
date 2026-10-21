class Solution:
    def minOperations(self, s: str) -> int:
        if s == "".join(sorted(s)):
            return 0
        
        n = len(s)
        if n == 2:
            return -1
            
        mn = min(s)
        mx = max(s)
        
        # 1 operation possible if min is at the start (proper prefix) or max is at the end (proper suffix)
        if (s[0] == mn and s != mn * n) or (s[-1] == mx and s != mx * n):
            return 1
            
        # Check if impossible to sort
        # If any proper prefix contains mn or any proper suffix contains mx, 3 operations might be needed.
        # Let's check conditions precisely based on bounds.
        has_mn_in_prefix = any(c == mn for c in s[:-1])
        has_mx_in_suffix = any(c == mx for c in s[1:])
        
        if not has_mn_in_prefix and not has_mx_in_suffix:
            return 3
            
        return 2