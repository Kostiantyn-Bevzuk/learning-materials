class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        bottom_row, right = len(matrix)-1, len(matrix[0])-1
        top_row = 0
        while top_row <= bottom_row:
            middle_row = (top_row + bottom_row) // 2
            if matrix[middle_row][0] == target:
                return True
            elif matrix[middle_row][0] < target:
                top_row = middle_row + 1
            elif matrix[middle_row][0] > target:
                bottom_row = middle_row - 1
        if bottom_row < 0:
            return False
        search_space = matrix[bottom_row]
        left = 0
        while left <= right:
            middle_pos = (left+right)//2
            if search_space[middle_pos] == target:
                return True
            elif search_space[middle_pos] > target:
                right = middle_pos - 1
            elif search_space[middle_pos] < target:
                left = middle_pos + 1
        return False


matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 4

[1, 2]

Solution().searchMatrix(matrix, target)