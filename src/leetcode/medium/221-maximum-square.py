# Top down approach


class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        cache = {}
        rows = len(matrix)
        cols = len(matrix[0])

        def dp(row, col) -> int:
            if row > rows - 1 or col > cols - 1:
                return 0
            if (row, col) in cache:
                return cache[(row, col)]
            if matrix[row][col] == "0":
                cache[(row, col)] = 0
                return 0
            else:
                cache[(row, col)] = 1 + min(
                    dp(row + 1, col), dp(row, col + 1), dp(row + 1, col + 1)
                )

            return cache[(row, col)]

        max_len = -float("inf")
        for row in range(rows):
            for col in range(cols):
                curr_max = dp(row, col)
                max_len = max(max_len, curr_max)

        return max_len**2 if max_len > 0 else 0


# Bottom up approach


class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])

        dp = Is that the same:
```
[[-float("inf")] * (cols ) for _ in range(rows)]

        for row in range(rows + 1):
            dp[row][-1] = 0
        for col in range(cols + 1):
            dp[-1][col] = 0

        for row in range(rows - 1, -1, -1):
            for col in range(cols - 1, -1, -1):
                if matrix[row][col] == "0":
                    dp[row][col] = 0
                else:
                    dp[row][col] = 1 + min(
                        dp[row + 1][col], dp[row][col + 1], dp[row + 1][col + 1]
                    )
        max_len = -float("inf")
        for row in range(rows):
            for col in range(cols):
                max_len = max(max_len, dp[row][col])

        return max_len**2