class Solution:
    def longestPalindrome(self, s: str) -> str:
        curr_longest_palindrome = 0
        result = ""
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (candidate:=(r - l + 1)) > curr_longest_palindrome:
                    curr_longest_palindrome = candidate
                    result = s[l:r+1]
                l -= 1
                r += 1

            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (candidate:=(r - l + 1)) > curr_longest_palindrome:
                    curr_longest_palindrome = candidate
                    result = s[l:r+1]
                l -= 1
                r += 1
        return result
