class Solution:
    storage = {0: 0, 1: 1} # TODO: move to __init__
    def fib(self, n: int) -> int:
        if n in self.storage:
            return self.storage[n]
        else:
            self.storage[n] = self.fib(n-2) + self.fib(n-1)
        return self.storage[n]



print(Solution().fib(4))
