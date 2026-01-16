class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        cache = {}
        wordSet = set(wordDict)

        def backtrack(index):
            if index == (len(s)):
                return True
            if index in cache:
                return cache[index]

            for i in range(index+1, len(s)+1):
                if s[index:i] in wordSet and backtrack(i):
                    cache[index] = True
                    return True
            cache[index] = False
            return False

        return backtrack(0)
    
# Bottom up approach 

class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        dp = [False for _ in range(len(s))]
        dp[-1] = True

        for i in range(len(s)-1, -1, -1):
            for w in wordDict:
                if i + len(w) <= len(s) and w == s[i: i + len(w)]:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break
        return dp[0]



# "leetcode"
# [False, False, False, False, False, False, False, True]
# 2, "le"
# 3, "lee"
# 4, "leet"
# 5, "c"


# Solution().wordBreak("catsandog", ["cats","dog","sand","and","cat"])
Solution().wordBreak("leetcode", ["leet", "code"])