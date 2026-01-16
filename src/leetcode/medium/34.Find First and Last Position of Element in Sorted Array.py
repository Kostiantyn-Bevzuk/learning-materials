# class Solution:
#     def searchRange(self, nums: list[int], target: int) -> list[int]:
#         left, right = 0, len(nums)-1

#         while left <= right:
#             middle = left + (right-left)//2
#             if nums[middle] == target:
#                 negative_path = positive_path = middle
#                 while negative_path >= 0 and nums[negative_path] == target:
#                     negative_path -= 1
#                 positive_path = middle + 1
#                 while positive_path <= len(nums) - 1 and nums[positive_path] == target:
#                     positive_path += 1

#                 return [negative_path, positive_path]

#             if nums[middle] > target:
#                 right = middle - 1
#             elif nums[middle] < target:
#                 left = middle + 1
#         return [-1, -1]

class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        left, right = 0, len(nums)-1
        first_occurance = -1
        last_occurance = -1
        while left <= right:
            middle = left + (right-left)//2
            if nums[middle] == target:
                first_occurance = middle
                right = middle - 1
            elif nums[middle] > target:
                right = middle - 1
            elif nums[middle] < target:
                left = middle + 1
        if first_occurance == -1:
            return [first_occurance, last_occurance]
        left, right = 0, len(nums)-1
        while left <= right:
            middle = left + (right-left)//2
            if nums[middle] == target:
                last_occurance = middle
                left = middle + 1
            elif nums[middle] > target:
                right = middle - 1
            elif nums[middle] < target:
                left = middle + 1


        return [first_occurance, last_occurance]
