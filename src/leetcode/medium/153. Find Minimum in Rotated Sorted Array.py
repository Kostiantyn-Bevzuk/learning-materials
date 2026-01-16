class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1

        while left <= right:
            middle = left + (right-left)//2
            if nums[left] <= nums[middle] <= nums[right]:
                return nums[left]
            if nums[left] <= nums[middle]: # sorted left part
                left = middle + 1
            if nums[right] > nums[middle]: # sorted right part
                right = middle
            

