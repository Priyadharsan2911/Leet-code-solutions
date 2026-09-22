class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        max_water = 0

        while left < right:
            # The width is the distance between pointers
            width = right - left
            
            # The height is bounded by the shorter line
            current_height = min(height[left], height[right])
            
            # Calculate and update maximum area
            current_water = width * current_height
            max_water = max(max_water, current_water)
            
            # Move the pointer pointing to the shorter height
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_water