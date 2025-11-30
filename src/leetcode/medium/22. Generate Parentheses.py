class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        current_comb = []

        def backtrack(open_count, closed_count):
            if open_count == closed_count == n:
                result.append("".join(current_comb))
                return

            if open_count <= n:
                current_comb.append("(")
                backtrack(open_count+1, closed_count)
                current_comb.pop()

            if closed_count < open_count:
                current_comb.append(")")
                backtrack(open_count, closed_count+1)
                current_comb.pop()

        backtrack(0, 0)
        return result
