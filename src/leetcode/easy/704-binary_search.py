class Solution:
    def search(self, nums: list[int], target: int) -> int:
        idx_l, idx_r = 0, len(nums) - 1
        while idx_l <= idx_r:
            new_idx = (idx_l + idx_r) // 2
            if nums[new_idx] == target:
                return new_idx
            elif nums[new_idx] > target:
                idx_r = new_idx - 1
            elif nums[new_idx] < target:
                idx_l = new_idx + 1
        return -1


nums = [-1, 0, 3, 5, 9, 12]
target = 2
solution = Solution()
print(solution.search(nums, target))
