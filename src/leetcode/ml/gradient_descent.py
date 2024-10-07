class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        if iterations <= 0:
            return init
        for step in range(iterations):
            init -= learning_rate * 2 * init
        return round(init, 5)
    

sol = Solution()
iterations = 0
learning_rate = 0.01
init = 5
print(sol.get_minimizer(iterations, learning_rate, init))