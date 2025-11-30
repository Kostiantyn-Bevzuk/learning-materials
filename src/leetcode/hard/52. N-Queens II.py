class Solution:
    def totalNQueens(self, n: int) -> int:
        output = [0]
        posdiag = {}
        negdiag = {}
        cols = set()

        def backtrack(row):
            if row == n:
                output[0] += 1
                return
            
            for col in range(n):
                if col in cols or col+row in posdiag or row - col in negdiag:
                    continue
                else:
                    cols.add(col)
                    posdiag.add(col+row)
                    negdiag.add(row-col)
                    backtrack(row+1)
                    cols.remove(col)
                    posdiag.remove(col+row)
                    negdiag(row-col)

        backtrack(0)

        return output[0]
