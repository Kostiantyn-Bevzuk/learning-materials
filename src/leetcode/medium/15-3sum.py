class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        interim_dict = dict()
        result = set()

        for i in range(len(nums)):
            target = 0
            target -= nums[i]
            interim_dict = dict()
            for j in range(i+1, len(nums)):
                if nums[j] in interim_dict:
                    interim_result = tuple(sorted([nums[i], nums[interim_dict[nums[j]]], nums[j]]))
                    result.add(interim_result)
                    continue
                interim_dict[target - nums[j]] = j
        return list(result)


print(Solution().threeSum([-1,0,1,2,-1,-4]))
# Exceed time limit