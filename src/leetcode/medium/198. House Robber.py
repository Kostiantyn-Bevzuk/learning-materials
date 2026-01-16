
# Bottom up approach

class Solution:
    def rob(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            if i - 2 < 0: # out of bounds
                nums[i] = max(nums[i-1], nums[i])
            else:
                nums[i] = max(nums[i-1], nums[i-2] + nums[i])

        return nums[-1]

# Recursive so called Top Down

class Solution:
    def rob(self, nums: List[int]) -> int:


        def helper(i):
            if i == 0:
                return nums[0]
            if i == 1:
                return max(nums[0], nums[1])
            
            return max(nums[i] + helper(i-2), helper(i-1))
        
        n = len(nums)

        return helper(n-1)
    
# Recursive Top Down (memoization)

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return nums[0]
        if n == 1:
            return max(nums[0], nums[1])

        cache = {0: nums[0], 1: max(nums[0], nums[1])}

        def helper(i):
            if i in cache:
                return cache[i]
            
            cache[i] = max(nums[i] + helper(i-2), helper(i-1))
            return cache[i]
        
        return helper(n-1)
