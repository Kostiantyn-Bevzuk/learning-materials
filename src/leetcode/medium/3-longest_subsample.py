# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         char_set = set()
#         l = 0
#         res = 0
#         for r in range(len(s)):
#             while s[r] in char_set:
#                 char_set.remove(s[l])
#                 l += 1
#             char_set.add(s[r])
#             res = max(res, r - l + 1) # max of result and curr window size
#         return res

# Use window function to find the longest substring without repeating characters


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        storage = {}
        l, r = 0, 0
        res = 0
        while r < len(s):
            if s[r] in storage:
                l = max(l, storage.get(s[r]) + 1)
            storage[s[r]] = r
            res = max(r-l+1, res)
            r += 1
            
        return res

r = 3
{"a" : 0,
 "b": 1,
 "c": 2,
 }
l = 1
r = 2

s = "tmmzuxt"
Solution().lengthOfLongestSubstring(s)