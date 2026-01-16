class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums)-1

        while left <= right:
            middle = left + (right - left) // 2 # to prevent overflow
            if nums[middle] == target:
                return middle

            if nums[middle] >= nums[left]: # sorted left part
                if nums[left] <= target <= nums[middle]:
                    right = middle - 1
                else:
                    left = middle + 1
            else: # right part sorted
                if nums[middle] <= target <= nums[right]:
                    left = middle + 1
                else:
                    right = middle - 1
        
        return -1

nums = [3,1]

Solution().search(nums, target=1)