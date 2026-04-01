class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        result = [0 for _ in range(len(nums))]
        for i in range(len(nums)):
            if nums[i] == 0:
                continue
            elif nums[i] > 0:
                step = (nums[i] + i) % len(nums)
            elif nums[i] < 0:
                step = (nums[i] + i) % -len(nums)
            result[i] = nums[step]
        return result