class Solution:
    def decodeString(self, s: str):
        if not s:
            return 
        numbers_set = {str(i) for i in range(10)}
        def decode(i: int) -> [str, int]:
            interim_res = ""
            modifier = []
            while i < len(s):
                if s[i] not in numbers_set and s[i] != "]":
                    interim_res += s[i]
                while s[i] in numbers_set:
                    modifier.append(s[i])
                    i += 1
                if modifier:
                    interim, i = decode(i + 1) # 2
                    interim_res += int("".join(modifier)) * interim
                    modifier = []
                elif s[i] == "]":
                    return interim_res, i
                i += 1
            return interim_res, i
        return decode(0)[0]
