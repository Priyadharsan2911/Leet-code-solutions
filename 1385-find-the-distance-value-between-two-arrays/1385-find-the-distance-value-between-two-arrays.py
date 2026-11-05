class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        arr2.sort()
        count = 0
        m = len(arr2)
        
        for x in arr1:
            # Binary search for the insertion point of x in sorted arr2
            left, right = 0, m - 1
            valid = True
            
            while left <= right:
                mid = (left + right) // 2
                if abs(arr2[mid] - x) <= d:
                    valid = False
                    break
                if arr2[mid] < x:
                    left = mid + 1
                else:
                    right = mid - 1
            
            # Also check the boundaries near the insertion point
            if valid:
                if left < m and abs(arr2[left] - x) <= d:
                    valid = False
                if left > 0 and abs(arr2[left - 1] - x) <= d:
                    valid = False
                    
            if valid:
                count += 1
                
        return count