"""
Given an array of integers nums and an integer target, 
return the indices of the two numbers that add up to the target. 
Each input is guaranteed to have exactly one solution, 
and you cannot use the same element more than once. 
"""
# O(n), memory O(2n) lim n-> inf -> O(n)
6

nums = [1, 2, 4, 6, 7]
def my_solution(nums: list[int], target: int):
    storage = {}
    for i in range(len(nums)):
        if nums[i] in storage:
            return i, storage[nums[i]]
        storage[target-nums[i]] = i


assert (2, 1) == my_solution(nums, 6)
assert (3, 0) == my_solution(nums, 7)

nums = [1, 3, -4, 6, 7]
def my_solution(nums: list[int], target: int):
    storage = {}
    for i, value in enumerate(nums):
        if value in storage:
            return i, storage[value]
        storage[target-value] = i

assert (2, 1) == my_solution(nums, -1)
