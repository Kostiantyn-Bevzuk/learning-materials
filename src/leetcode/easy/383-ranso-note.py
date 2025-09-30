class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        storage = {}
        for c in magazine:
            storage[c] = storage.get(c, 0) + 1
        for c in ransomNote:
            if c in storage:
                storage[c] -= 1
                if storage[c] == 0:
                    del storage[c]
            else:
                return False
        return True

ransomNote = "aa"
magazine = "ab"

Solution().canConstruct(ransomNote, magazine)