
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def construct(self, grid: list[list[int]]) -> 'Node':
        def dfs(n, row, col): # len(grid), 0, 0
            all_the_same = True
            for curr_row in range(n):
                for curr_col in range(n):
                    if grid[row][col] != grid[row+curr_row][col+curr_col]:
                        all_the_same = False

            if all_the_same:
                return Node(val = grid[row][col], isLeaf=True) # all others are None

            n = n//2
            top_left = dfs(n, row, col)
            top_right = dfs(n, row, col+n)
            bottom_left = dfs(n, row+n, col)
            bottom_right = dfs(n, row+n, col+n)
            return Node(
                val=1,
                isLeaf=False,
                topLeft=top_left,
                topRight=top_right,
                bottomLeft=bottom_left,
                bottomRight=bottom_right
                )
        
        return dfs(len(grid), 0, 0)
