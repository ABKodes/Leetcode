class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        left , right = 0, len(heights) - 1
        while left < right:
            area = max(area, (right - left) * min(heights[left], heights[right])) 
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return area