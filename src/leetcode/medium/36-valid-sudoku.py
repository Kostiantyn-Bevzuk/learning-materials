class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        storage_vertical = {}
        storage_horizontal = {}
        storage_square = {}
        for i in range(9):
            storage_horizontal[i] = set()
            storage_vertical[i] = set()
            for j in range(9):
               storage_square[(int(i/3), int(j/3))] = set()

        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue
                if board[row][col] in storage_horizontal[row]:
                    return False
                else:
                    storage_horizontal[row].add(board[row][col])
                if board[row][col] in storage_vertical[col]:
                    return False
                else:
                    storage_vertical[col].add(board[row][col])
                if board[row][col] in storage_square[(int(row/3), int(col/3))]:
                    return False
                else:
                    storage_square[(int(row/3), int(col/3))].add(board[row][col])
        return True

board = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]
Solution().isValidSudoku(board)
