class Solution:
    def jump(self, nums: list[int]) -> int:
        result = 0
        l = 0
        r = max_step = nums[0]
        while r < len(nums):
            for i in range(l, r+1):
                max_step = max(max_step, nums[i] + i)
            result += 1
            l += 1
            r = max_step
        return result

nums = [2,3,1,1,4]

Solution().jump(nums)
