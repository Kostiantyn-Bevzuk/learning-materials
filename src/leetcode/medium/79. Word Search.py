class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        board_rows = len(board)
        board_cols = len(board[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visited = set()

        def backtracking(index, row, col):
            if (
                row < 0
                or col < 0
                or (row > board_rows - 1)
                or (col > board_cols - 1)
                or ((row, col) in visited)
                or (index == len(word))
                or (board[row][col] != word[index])
            ):
                return False
            elif index == len(word)-1:
                return True

            visited.add((row, col))

            for direction in directions:
                new_row = row + direction[0]
                new_col = col + direction[1]
                if backtracking(index+1, new_row, new_col):
                    return True
            visited.remove((row, col))

            return False



        for row in range(board_rows):
            for col in range(board_cols):
                if backtracking(0, row, col):
                    return True

        return False


