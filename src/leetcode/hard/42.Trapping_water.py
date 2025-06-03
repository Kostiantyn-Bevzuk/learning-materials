class Solution:
    def trap(self, height: list[int]) -> int:
        if len(height) == 0:
            return 0
        trapped_water = 0
        max_left = [0]
        max_right = [0]
        for i in range(0, len(height)-1):
            max_left.append(max(max_left[i], height[i]))
        for i in range(len(height)-1, 0, -1):
            max_right.append(max(max_right[-1], height[i]))
        
        max_right = max_right[::-1]

        for i in range(len(height)):
            trapped_water += max(min(max_right[i], max_left[i]) - height[i], 0)

        return trapped_water

Solution().trap([4,2,0,3,2,5])

# class Solution:
    # def trap(self, height: list[int]) -> int:
    #     if len(height) == 0:
    #         return 0
    #     trapped_water = 0
    #     max_left = 0
    #     max_right = 0
    #     l, r = 0, len(height)-1
    #     while l < r:
    #         trapped_water += max(min(max_left, max_right) - height[l], 0)
    #         max_left = height[l]
    #         max_right = height[r]
    #         if max_left > max_right:
    #             r -= 1
    #         else:
    #             l += 1

        