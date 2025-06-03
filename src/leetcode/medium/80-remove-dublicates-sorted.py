class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        l, r = 0, 0
        while l < len(nums) and r < len(nums):
            counter = 1
            while r < len(nums) - 1 and nums[r] == nums[r+1]:
                counter += 1
                r += 1
            for _ in range(min(2, counter)):
                nums[l] = nums[r]
                l += 1
            r += 1
        return l



test = [0,0,1,1,1,1,2,3,3]
Solution().removeDuplicates(test)