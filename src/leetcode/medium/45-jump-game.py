class Solution:
    def jump(self, nums: list[int]) -> int:
        res = 0
        l = r = 0
        while r < len(nums)-1:
            max_step = 0
            for i in range(l, r+1):
                max_step = max(max_step, i + nums[i])
            l = r+1
            r = max_step
            res += 1
        return res




nums = [2,3,1,1,4]
nums = [10,9,8,7,6,5,4,3,2,1,1,0]

print(Solution().jump(nums))
