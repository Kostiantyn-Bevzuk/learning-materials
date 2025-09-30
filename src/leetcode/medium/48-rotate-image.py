class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l, r = 0, len(matrix)-1
        top, bottom = 0, len(matrix)-1
        tmp_value = 0
        while top < bottom:
            offset = 0
            while offset < r-l:
                tmp_value = matrix[top][l+offset] # 2
                matrix[top+offset][r], tmp_value = tmp_value, matrix[top+offset][r]
                matrix[bottom][r-offset], tmp_value = tmp_value, matrix[bottom][r-offset]
                matrix[bottom-offset][l], tmp_value = tmp_value, matrix[bottom-offset][l]
                matrix[top][l+offset], tmp_value = tmp_value, matrix[top][l+offset]
                offset += 1
            top += 1
            bottom -= 1
            l += 1
            r -= 1
        return matrix
                

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

print(Solution().rotate(matrix))