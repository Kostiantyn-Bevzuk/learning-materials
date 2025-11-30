from collections import deque

class Solution:
    def snakesAndLadders(self, board: list[list[int]]) -> int:
        length = len(board) # 6
        visited = {1}
        queue = deque()
        queue.append(1)
        min_number = 0

        while queue:
            min_number += 1
            for _ in range(len(queue)):
                last_turn = queue.popleft() # 1
                for dice_roll in range(1, 7):
                    nxt = last_turn + dice_roll
                    if nxt > length**2:
                        continue
                    row, col = self.get_position(nxt, length) # pos on board
                    if (ladder_or_snake :=board[row][col]) != -1:
                        nxt = ladder_or_snake
                    if nxt == length**2:
                        return min_number
                    if nxt not in visited:
                        visited.add(nxt)
                        queue.append(nxt)
        return -1

    @staticmethod
    def get_position(index: int, length) -> tuple[int, int]:
        row = (index-1) // length
        matrix_row = length - row - 1
        matrix_col = (index-1) % length
        if row % 2 == 1: # reversed order
            matrix_col = length - matrix_col - 1

        return matrix_row, matrix_col


board =[[2,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1]]

Solution().snakesAndLadders(board)