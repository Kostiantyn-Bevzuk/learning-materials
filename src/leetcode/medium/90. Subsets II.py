from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()

        curr_comb = []

        def backtrack(index):
            ans.append(curr_comb[:])

            for i in range(index, len(nums)):
                
                if i > index and nums[i] == nums[i-1]:
                    continue
                else:
                    curr_comb.append(nums[i])
                    backtrack(i+1)
                    curr_comb.pop()
        
        backtrack(0)
        return ans
    
Solution().subsetsWithDup([2, 2, 2])    

# [1, 2, 2]
# []
# [1] (1, 3)
# [1, 2] (2, 3)
# [1, 2, 2] (3, 3)
# [2] (2, 3)
# [2, 2] (3, 3)
# [2] # (3, 3)

     
# [2, 2, 2, 2]
# []
# [2]
# [2, 2]
# [2, 2, 2]
