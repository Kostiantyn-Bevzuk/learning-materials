class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        for elem1, elem2 in zip(x_str, reversed(x_str)):
            if elem1 == elem2:
                continue
            else:
                return False
        return True