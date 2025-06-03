# Dict solution
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        storage = {}
        for idx in range(len(numbers)):
            if numbers[idx] in storage:
                return [storage[numbers[idx]]+1, idx+1]
            storage[target-numbers[idx]] = idx


# Solution().twoSum(numbers = [2,3,4], target = 6)


# Two pointers solution
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l, r = 0, len(numbers)-1
        while l < r:
            summ = numbers[l] + numbers[r]
            if summ > target:
                r -= 1
            elif target == summ:
                return [l+1, r+1]
            else:
                l += 1

Solution().twoSum(numbers = [2,3,4,5], target = 6)