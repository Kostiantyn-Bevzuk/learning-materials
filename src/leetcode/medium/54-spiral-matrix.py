import numpy as np

class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        result = []
        matrix = np.array(matrix)
        while matrix.size:
            matrix, result = self.spiral_recurse(matrix, result)
        return result

    @staticmethod
    def spiral_recurse(matrix, result):
        m = len(matrix)
        n = len(matrix[0])
        if m == 1:
            for col in range(n):
                result.append(int(matrix[0][col]))
            return np.array([]), result
        middle_part = m - 2
        for col in range(n):
            result.append(int(matrix[0][col]))
        for row in range(1, middle_part+1):
            result.append(int(matrix[row][-1]))
        for col in range(n-1, -1, -1):
            result.append(int(matrix[-1][col]))
        if n > 1:
            for row in range(middle_part, 0, -1):
                result.append(int(matrix[row][0]))
        matrix = matrix[1: -1, 1: -1]
        return matrix, result

        
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# matrix = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

print(Solution().spiralOrder(matrix))