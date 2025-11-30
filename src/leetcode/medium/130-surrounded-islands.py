from collections import deque


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def bfs(row, col):
            queue = deque()
            queue.append((row, col))

            while queue:
                curr_row, curr_col = queue.popleft()
                for dr in directions:
                    r, c = curr_row + dr[0], curr_col + dr[1]
                    if (
                        0 <= r < rows and
                        0 <= c < cols and
                        board[r][c] == "O"
                        ):
                        board[r][c] = "T"
                        queue.append((r, c))

        for row in [0, rows-1]:
            for col in range(cols):
                if board[row][col] == "O":
                    board[row][col] = "T"
                    bfs(row, col)

        for row in range(rows):
            for col in [0, cols-1]:
                if board[row][col] == "O":
                    board[row][col] = "T"
                    bfs(row, col)

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O":
                    board[row][col] = "X"

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "T":
                    board[row][col] = "O"

