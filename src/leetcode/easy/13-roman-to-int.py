class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900
        }
        indx = 0
        result = 0
        while indx < len(s):
            if indx == len(s)-1:
                result += values.get(s[indx])
                indx +=1
            else:
                value_to_add = values.get(s[indx]+s[indx+1])
                result += value_to_add if value_to_add else values.get(s[indx])
                indx += 2 if value_to_add else 1
        return result

print(Solution().romanToInt("CM"))

