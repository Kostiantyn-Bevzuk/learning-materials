class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        while i < len(haystack) - len(needle)+1:
            if haystack[i:i+len(needle)] == needle:
                return i
            i += 1
        return -1
    
haystack = "leetcode"
needle = "leeto"
print(Solution().strStr(haystack=haystack, needle=needle))