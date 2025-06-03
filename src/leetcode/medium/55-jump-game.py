class Solution:
    def canJump(self, nums: list[int]) -> bool:
        i = 0
        step = nums[i]
        while i < len(nums)-1:
            if step:
                i += 1
                step -= 1
                step = max(step, nums[i])
            else:
                return False
        return True



nums = [2,3,1,1,4]
# nums = [3,2,1,0,4]

print(Solution().canJump(nums))