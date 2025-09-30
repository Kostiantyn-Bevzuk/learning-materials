class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 0-0 -> 0; 1-0 -> 1; 0-1 -> 2; 1-1 ->3
        ROWS, COLS = len(board), len(board[0])
        for row in range(ROWS):
            for col in range(COLS):
                countneightbors = self.calculate_neighbours(row, col, board)

                if board[row][col]:  # equal to 1
                    if countneightbors in [2, 3]:
                        board[row][col] = 3
                    else:
                        board[row][col] = 1
                else:  # equal to 0
                    if countneightbors == 3:
                        board[row][col] = 2
                    else:
                        board[row][col] = 0

        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == 1:
                    board[row][col] = 0
                elif board[row][col] in [2, 3]:
                    board[row][col] = 1

    @staticmethod
    def calculate_neighbours(curr_row, curr_col, board):
        counter = 0
        for row in range(curr_row - 1, curr_row + 2):
            for col in range(curr_col - 1, curr_col + 2):
                if (
                    row < 0
                    or col < 0
                    or row >= len(board)
                    or col >= len(board[0])
                    or (row == curr_row and col == curr_col)
                ):
                    continue
                if board[row][col] in [1, 3]:
                    counter += 1

        return counter
