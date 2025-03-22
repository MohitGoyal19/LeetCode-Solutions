class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        left, right = 0, len(height) - 1

        while left < right:
            area = max(min(height[left], height[right]) * abs(right-left), area)

            if height[left] < height[right]:
                left += 1

            else:
                right -= 1 

        return area