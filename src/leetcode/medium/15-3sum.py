class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []
        nums.sort()
        for indx, val in enumerate(nums):
            if indx > 0 and val == nums[indx-1]:
                continue
            target = - val
            i, j = indx+1, len(nums)-1
            while i < j:
                if nums[i] + nums[j] > target:
                    j -= 1
                elif nums[i] + nums[j] < target:
                    i += 1
                else:
                    result.append([val, nums[i], nums[j]])
                    i += 1
                    while nums[i] == nums[i-1] and i < j:
                        i += 1
        return result


nums = [2,-3,0,-2,-5,-5,-4,1,2,-2,2,0,2,-4,5,5,-10]

print(Solution().threeSum(nums))

