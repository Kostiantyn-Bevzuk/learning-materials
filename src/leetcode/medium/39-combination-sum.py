class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []
        curr_comb = []

        def backtrack(index, counter):
            if counter == target:
                result.append(curr_comb[:])
                return
            elif counter > target:
                return

            for i in range(index, len(candidates)):
                number = candidates[i]
                curr_comb.append(number)
                backtrack(i, counter+number)
                curr_comb.pop()

        backtrack(0, 0)
        return result
