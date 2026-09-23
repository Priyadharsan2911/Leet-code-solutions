class Solution:
    def minOperations(self, grid: list[list[int]], x: int) -> int:
        # Flatten the 2D grid into a 1D list
        vals = [val for row in grid for val in row]
        
        # Check if all elements can be made equal
        remainder = vals[0] % x
        for val in vals:
            if val % x != remainder:
                return -1
        
        # Sort values to find the median
        vals.sort()
        median = vals[len(vals) // 2]
        
        # Calculate total operations needed to convert all values to median
        return sum(abs(val - median) // x for val in vals)