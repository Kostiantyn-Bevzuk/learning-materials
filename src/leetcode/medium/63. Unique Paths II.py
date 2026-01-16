# Top down

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        cache = {(0, 0): 1}
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        if obstacleGrid[0][0] or obstacleGrid[rows-1][cols-1]:
            return 0

        def dp(row, col): # Number of unique path to current position
            if (row, col) in cache:
                return cache[(row, col)]

            if row < 0 or col < 0:
                return 0

            if obstacleGrid[row][col] == 1:
                return 0

            cache[(row, col)] = dp(row-1, col) + dp(row, col-1)
            return cache[(row, col)]

        return dp(rows-1, cols-1)
# Bottom up

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])

        if obstacleGrid[0][0] or obstacleGrid[rows-1][cols-1]:
            return 0

        for row in range(rows):
            for col in range(cols):
                if row == 0 and col == 0:
                    obstacleGrid[row][col] = 1
                elif obstacleGrid[row][col] == 1:
                    obstacleGrid[row][col] = 0
                elif row - 1 < 0:
                    obstacleGrid[row][col] = obstacleGrid[row][col-1]
                elif col - 1 < 0:
                    obstacleGrid[row][col] = obstacleGrid[row - 1][col]
                else:
                    obstacleGrid[row][col] = obstacleGrid[row][col-1] + obstacleGrid[row-1][col]
        return obstacleGrid[rows-1][cols-1]
        
obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]

Solution().uniquePathsWithObstacles(obstacleGrid)