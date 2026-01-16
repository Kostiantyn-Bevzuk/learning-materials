class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return 0
        left, right = 0, len(nums)-1

        while left <= right:
            middle_indx = (left+right) // 2
            if left == right:
                return middle_indx

            if nums[middle_indx] < nums[middle_indx+1]:
                left = middle_indx + 1
            else:
                right = middle_indx


# class Solution:
#     def findPeakElement(self, nums: list[int]) -> int:
#         if len(nums) == 1:
#             return 0
#         left, right = 0, len(nums)-1

#         while left <= right:
#             middle_indx = left + (right-left) // 2 # To prevent overflow
#             if middle_indx > 0 and nums[middle_indx] < nums[middle_indx-1]:
#                 right = middle_indx - 1
#             elif middle_indx < len(nums) and nums[middle_indx] > nums[middle_indx+1]:
#                 left = middle_indx + 1
#             else:
#                 return middle_indx


nums = [1, 2, 3, 1]

Solution().findPeakElement(nums)