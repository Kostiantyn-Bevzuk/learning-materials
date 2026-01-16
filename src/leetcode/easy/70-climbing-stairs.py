class Solution:
    def climbStairs(self, n: int) -> int:
        cache: dict[int, int] = {}

        def backtrack(stair: int) -> int:
            if stair > n:
                return 0
            if stair == n:
                return 1
            if stair in cache:
                return cache[stair]

            cache[stair] = backtrack(stair + 1) + backtrack(stair + 2)
            return cache[stair]

        return backtrack(0)


Solution().climbStairs(n=5)