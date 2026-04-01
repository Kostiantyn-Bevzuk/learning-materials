class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        longest_seq = 0
        occured_zero_index = []
        l = r = 0
        while r < len(nums):
            while r < len(nums) and nums[r] == 1:
                longest_seq = max(longest_seq, r-l+1)
                r += 1
            if k > 0:
                occured_zero_index.append(r)
                longest_seq = max(longest_seq, r-l+1)
                r += 1
                k -= 1
            else:
                l = occured_zero_index.pop(0) + 1
                occured_zero_index.append(r)
                r += 1
        return longest_seq
            
nums = [1,1,1,0,0,0,1,1,1,1,0]

Solution().longestOnes(nums, 2)

