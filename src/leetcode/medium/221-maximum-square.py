class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        cache = {}
        rows = len(matrix)
        cols = len(matrix[0])

        def dp(row, col) -> int:
            if row >= rows or col >= cols:
                return 0
            
            
