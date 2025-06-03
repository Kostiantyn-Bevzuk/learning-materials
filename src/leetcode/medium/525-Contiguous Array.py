class Solution:
    def findMaxLength(self, nums: list[int]) -> int:
        # 101010
        zero, one = 0, 0
        res = 0

        storage = {}
        for indx, val in enumerate(nums):
            if val == 0:
                zero += 1
            else:
                one += 1
            diff = one - zero
            if one == zero:
                res = one+zero
            if diff in storage:
                res = max(res, indx - storage[diff])
            else:
                storage[diff] = indx
            if one == zero:
                res = one+zero
        return res
