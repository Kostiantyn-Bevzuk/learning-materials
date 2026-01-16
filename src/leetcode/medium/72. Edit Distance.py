# Top down

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        cache = {}

        def dp(i, j):
            if (i, j) in cache:
                return cache[(i, j)]
            if i == len(word1) and j == len(word2):
                return 0
            
            elif i == len(word1) and j != len(word2):
                return len(word2) - j
            
            elif i != len(word1) and j == len(word2):
                return len(word1) - i


            if word1[i] == word2[j]:
                cache[(i, j)] = dp(i+1, j+1)
            else:
                cache[(i, j)] = 1 + min(dp(i, j+1), dp(i+1, j), dp(i+1, j+1))

            return cache[(i, j)]

        return dp(0, 0)
    
# Solution().minDistance(word1="horse", word2="ros")

# Bottom up

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        rows = len(word1)
        cols = len(word2)
        dp = [[float("inf")] * (cols + 1) for _ in range(rows+1)]

        for row in range(rows, -1, -1):
            dp[row][-1] = rows - row
        
        for col in range(cols, -1, -1):
            dp[-1][col] = cols - col
        
        for row in range(rows-1, -1, -1):
            for col in range(cols-1, -1, -1):
                if word1[row] == word2[col]:
                    dp[row][col] = dp[row+1][col+1]
                else:
                    dp[row][col] = 1 + min(dp[row+1][col], dp[row][col+1], dp[row+1][col+1])

        return dp[0][0]

Solution().minDistance(word1="horse", word2="ros")
        