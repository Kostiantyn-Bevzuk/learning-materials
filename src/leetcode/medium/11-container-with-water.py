class Solution:
    def maxArea(self, height: list[int]) -> int:
        curr_max_water_stored = 0
        start, end = 0, len(height) - 1
        while start < end:
            lowest_water_level = min(height[start], height[end])
            curr_max_water_stored = max(
                curr_max_water_stored,
                lowest_water_level * (end-start)
                )
            if height[start] <= height[end]:
                start += 1
            else:
                end -= 1
        return curr_max_water_stored
    

height = [1,8,6,2,5,4,8,3,7]

print(Solution().maxArea(height))