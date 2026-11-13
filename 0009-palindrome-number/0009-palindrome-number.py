class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers are not palindromes (e.g., -121 -> 121-)
        # Numbers ending in 0 (except 0 itself) are not palindromes (e.g., 10 -> 01)
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10
            
        # When the length is odd, we can get rid of the middle digit by reversed_half // 10
        # e.g. for 12321, at the end of the loop: x = 12, reversed_half = 123
        return x == reversed_half or x == reversed_half // 10