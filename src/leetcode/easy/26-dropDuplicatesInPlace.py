class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        l = 1
        for indx in range(l, len(nums)-1):
            if nums[indx] == nums[indx+1]:
                continue
            elif nums[indx] != nums[indx+1]:
                nums[l] = nums[indx+1]
                l += 1
        return l




inp = [0,0,1,1,1,2,2,3,3,4]
print(Solution().removeDuplicates(inp))