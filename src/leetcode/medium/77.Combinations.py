class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        result = []
        current_comb = []
        def backtrack(index):
            if len(current_comb) == k:
                result.append(current_comb[:])
                return

            for number in range(index, n+1):
                current_comb.append(number)
                backtrack(number+1)
                current_comb.pop()
        backtrack(1)
        return result

Solution().combine(4, 2)