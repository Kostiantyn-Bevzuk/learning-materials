class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        interim_result = []
        def backtrack(index):
            if index > len(nums):
                return
            result.append(interim_result[:])
            for idx in range(index, len(nums)):
                interim_result.append(nums[idx])
                backtrack(idx+1)
                interim_result.remove(nums[idx])
        
        backtrack(0)
        return result
