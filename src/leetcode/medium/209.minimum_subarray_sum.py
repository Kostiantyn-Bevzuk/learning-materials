class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        l, r = 0, 0
        res = float("inf")
        summ = 0
        while r < len(nums):
            if summ < target:
                summ += nums[r]
                r += 1
            while summ >= target:
                summ -= nums[l]
                res = min(r-l, res)
                l += 1
        return res if res != float("inf") else 0
            
    
target = 7
nums = [2,3,1,2,4,3]

Solution().minSubArrayLen(target, nums)