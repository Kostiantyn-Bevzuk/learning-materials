class Solution:
    def reverseWords(self, s: str) -> str:
        splitted_arr = s.split(" ")
        splitted_arr = [elem for elem in splitted_arr if elem]
        splitted_arr = " ".join(splitted_arr[::-1])
        return splitted_arr


print(Solution().reverseWords("  hello world  "))