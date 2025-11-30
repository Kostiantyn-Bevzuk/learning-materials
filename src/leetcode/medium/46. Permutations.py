class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []
        current_solution = []

        def bakctrack():
            if len(current_solution) == len(nums):
                result.append(current_solution[:])
                return

            for indx in range(len(nums)):
                if nums[indx] not in current_solution:
                    current_solution.append(nums[indx])
                    bakctrack()
                    current_solution.pop()

        bakctrack()

        return result

