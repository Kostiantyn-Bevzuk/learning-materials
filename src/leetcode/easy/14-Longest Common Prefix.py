class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        res = ""
        initial_word = strs[0]
        for indx in range(len(initial_word)):
            for word in strs:
                if word[indx] != initial_word[indx] or indx >= len(word) or indx >= len(initial_word):
                    return res
                elif word[indx] == initial_word[indx]:
                    continue
            res += initial_word[indx]
        return res


strs = ["flower","flow","flight"]

print(Solution().longestCommonPrefix(strs))