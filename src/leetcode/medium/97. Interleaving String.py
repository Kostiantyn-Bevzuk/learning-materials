# Top Down

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        cache = {}
        if not s1:
            return s2 == s3
        elif not s2:
            return s1 == s3
        if len(s1) + len(s2) != len(s3):
            return False

        def dp(s1_pointer, s2_pointer) -> bool:
            s3_pointer = s1_pointer + s2_pointer
            if s1_pointer == len(s1) and s2_pointer == len(s2):
                return True

            if (s1_pointer, s2_pointer) in cache:
                return cache[(s1_pointer, s2_pointer)]

            if (s1_pointer <= len(s1) - 1 and s1[s1_pointer] == s3[s3_pointer]) and (s2_pointer <= len(s2) - 1 and s2[s2_pointer] == s3[s3_pointer]):
                cache[(s1_pointer, s2_pointer)] = dp(s1_pointer+1, s2_pointer) or dp(s1_pointer, s2_pointer+1)
                return dp(s1_pointer+1, s2_pointer) or dp(s1_pointer, s2_pointer+1)

            if s1_pointer <= len(s1) - 1 and s1[s1_pointer] == s3[s3_pointer]:
                cache[(s1_pointer, s2_pointer)] = dp(s1_pointer+1, s2_pointer)
                return dp(s1_pointer+1, s2_pointer)
            if s2_pointer <= len(s2) - 1 and s2[s2_pointer] == s3[s3_pointer]:
                cache[(s1_pointer, s2_pointer)] = dp(s1_pointer, s2_pointer+1)
                return dp(s1_pointer, s2_pointer+1)
            else:
                cache[(s1_pointer, s2_pointer)] = False
                return False

        return dp(0, 0)
    
# Bottom up

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if not s1:
            return s2 == s3
        elif not s2:
            return s1 == s3
        if len(s1) + len(s2) != len(s3):
            return False
        
        dp = [[False] * (len(s2)+1) for _ in range(len(s1) + 1)]   
        dp[len(s1)][len(s2)] = True
        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                k = i + j
                if i < len(s1) and s3[k] == s1[i] and dp[i+1][j]:
                    dp[i][j] = True
                if j < len(s2) and s3[k] == s2[j] and dp[i][j+1]:
                    dp[i][j] = True
        
        return dp[0][0]

    
s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbbaccc"
Solution().isInterleave(s1, s2, s3)