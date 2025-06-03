class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        l, r = 0, len(nums) - 1
        while r >= l:
            if nums[r] == val:
                r -= 1
            if nums[l] == val:
                nums[l] = nums[r]
                nums[r] = "_"
                r -= 1
            l += 1
        return r+1
    
# Just use 2 pointers.

Solution().removeElement(nums=[0,1,2,2,3,0,4,2], val=2)