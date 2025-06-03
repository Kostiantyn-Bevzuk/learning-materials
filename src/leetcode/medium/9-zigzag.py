class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        res = ""
        for i in range(numRows):
            step = numRows + (numRows-2)
            for j in range(i, len(s), step):
                res += s[j]
                if i > 0 and i < numRows-1 and j + step - 2*i  < len(s):
                    res += s[j + step - 2*i]
        return res

print(Solution().convert("PAYPALISHIRING", 5))