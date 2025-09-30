class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while i < len(t) and j < len(s):
            if t[i] == s[j]:
                if j == len(s)-1:
                    return True
                j += 1
                i += 1
            else:
                i += 1
        return False

s = "axc"
t = "ahbgdc"
Solution().isSubsequence(s=s, t=t)