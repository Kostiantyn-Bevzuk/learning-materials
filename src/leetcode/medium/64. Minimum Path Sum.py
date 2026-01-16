# Top down approach

class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        cache = {}
        rows = len(grid)
        cols = len(grid[0])

        def dp(row, col):
            if row == rows-1 and col == cols-1:
                return grid[row][col]
            if row >= rows or col >= cols:
                return float("inf")

            if (row, col) in cache:
                return cache[(row, col)]
            
            cache[(row, col)] = grid[row][col] + min(dp(row+1, col), dp(row, col+1))
            return cache[(row, col)]

        return dp(0, 0)
    
# Bottom up approach:

class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        for row in range(rows-2, -1, -1):
            grid[row][-1] = grid[row+1][-1] + grid[row][-1] 
        
        for col in range(cols-2, -1, -1):
            grid[-1][col] = grid[-1][col+1] + grid[-1][col] 

        for row in range(rows-2, -1, -1):
            for col in range(cols-2, -1, -1):
                grid[row][col] = grid[row][col] + min(grid[row][col+1], grid[row+1][col])
        
        return grid[0][0]
    
grid = [[1,3,1],[1,5,1],[4,2,1]]

Solution().minPathSum(grid)