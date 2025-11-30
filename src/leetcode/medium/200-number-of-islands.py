from collections import deque

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        island_counter = 0
        rows, cols = len(grid), len(grid[0])

        def bfs(row, col):
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            queue = deque()
            queue.append((row, col))

            while queue:
                curr_row, curr_col = queue.popleft()
                for dr in directions:
                    r, c = curr_row+dr[0], curr_col+dr[1]
                    if (
                        0 <= r < rows and
                        0 <= c < cols and
                        grid[r][c] == "1"
                        ):
                        grid[r][c] = "2"
                        queue.append((r, c))

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    island_counter += 1
                    grid[row][col] = "2"
                    bfs(row, col, grid)


        return island_counter
