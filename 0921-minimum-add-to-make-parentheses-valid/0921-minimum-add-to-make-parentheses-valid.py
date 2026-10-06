class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_count = 0
        moves = 0
        
        for char in s:
            if char == '(':
                open_count += 1
            else:
                if open_count > 0:
                    open_count -= 1
                else:
                    moves += 1
                    
        return moves + open_count