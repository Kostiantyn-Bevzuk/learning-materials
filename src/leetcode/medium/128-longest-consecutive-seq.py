class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        storage = set(nums)
        result = 0
        for value in nums:
            if (value - 1) not in storage:
                length = 1
                while (value + length) in storage: 
                    length += 1
                result = max(result, length)
        return result



# class Solution:
#     def longestConsecutive(self, nums: list[int]) -> int:
#         storage = {}
#         result = 0
#         nums = set(nums)
#         for val in nums:
#             before = storage.get(val-1, 0)
#             after = storage.get(val+1, 0)
#             max_length = before+after+1
#             result = max(max_length, result)
#             storage[val-before] = max_length
#             storage[val+after] = max_length
#         return result


nums = [1,0,1,2]

Solution().longestConsecutive(nums)