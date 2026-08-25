class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_water = 0

        while left < right:
            
            # Update max water if current container is larger
            current_water = min(heights[left], heights[right])*(right - left)
            max_water = max(max_water, current_water)
            
            # Move the pointer pointing to the shorter bar
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
                
        return max_water