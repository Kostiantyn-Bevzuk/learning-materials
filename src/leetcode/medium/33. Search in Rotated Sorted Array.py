class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l+r) // 2 # 0, 5 = 2; 3, 5 = 4
            if nums[mid] == target:
                return mid
            # we look which part is sorted
            if nums[mid] >= nums[l]:
                # left side is sorted
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
                    # move to the left side
            elif nums[r] > nums[mid]:
                # right side is sorted
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1
        

# [4, 5, 6, 7, 0, 1, 2] # 0
# # [0, 1, 2, 4, 5, 6, 7]
# [6, 7, 0, 1, 2, 4, 5]
# [4, 7, 2] # nums[mid] - nums[l] if > 0 left side monotonically increase -> if target between values where it is monotonically increasing if yes -> move there, else choose other side
# [6, 1, 5] # nums[r] - nums[mid] if > 0 right side monotonically increase

nums = [4,5,6,7,0,1,2]

Solution().search(nums, target=0)