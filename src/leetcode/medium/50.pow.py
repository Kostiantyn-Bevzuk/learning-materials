class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        
        memoization = {0: 1, 1: x}
        
        def backtrack(n):
            if n == 0:
                return memoization[n]
            elif n == 1:
                return memoization[n]
            elif n in memoization:
                return memoization[n]
            
            if n % 2 == 1:
                memoization[n] = x * backtrack(n//2) ** 2
                return memoization[n]
            else:
                memoization[n] = backtrack(n//2) ** 2
                return memoization[n]

        if n == 0:
            return 1
        elif n < 0:
            return 1/backtrack(abs(n))
        else:
            return backtrack(n)
# Correct but getting overflow error because of power function


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        
        def backtrack(n):
            if n == 0:
                return 0
            elif n == 1:
                return x

            result = backtrack(n//2)
            result = result * result
            return result * x if n%2 else result

        if n == 0:
            return 1
        elif n < 0:
            return 1/backtrack(abs(n))
        else:
            return backtrack(n)