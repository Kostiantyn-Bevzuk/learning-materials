class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        candidate = "".join(re.findall(r"[a-zA-Z0-9]", s)).lower()
        print(candidate)
        i, j = 0, len(candidate)-1
        while i < j:
            if candidate[i] == candidate[j]:
                i += 1
                j -= 1
            else:
                return False
        return True


s = "ab_a"
print(Solution().isPalindrome(s))