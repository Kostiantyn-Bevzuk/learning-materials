# Top down approach

class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        cache = {0: 1}

        def dp(i):
            if i in cache:
                return cache[i]
            max_value = 1
            for j in range(i):
                if nums[j] < nums[i]:
                    max_value = max(max_value, dp(j) + 1)
            cache[i] = max_value
            return cache[i]
        return max(dp(i) for i in range(len(nums)))
    
# Bottom up

class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        if not nums:
            return
        dp = [1 for _ in range(len(nums))]
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], 1 + dp[j])
                
        return max(dp)


nums = [10,9,2,5,3,7,101,18]

Solution().lengthOfLIS(nums)