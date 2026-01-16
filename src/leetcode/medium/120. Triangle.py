# Top Down

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        cache = {}

        def dp(index, layer_index):
            if (index, layer_index) in cache:
                return cache[(index, layer_index)]
            if layer_index >= len(triangle):
                return 0

            cache[(index, layer_index)] = triangle[layer_index][index] + min(dp(index, layer_index+1), dp(index+1, layer_index+1))
            return cache[(index, layer_index)]

        return dp(0, 0)


# Bottom up
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # dp = [0 for _ in range(triangle[-2])]

        for row in range(len(triangle)-2, -1, -1):
            for i in range(1, len(triangle[row+1])):
                triangle[row][i-1] = triangle[row][i-1] + min(triangle[row+1][i-1], triangle[row+1][i])
        
        return triangle[0][0]
