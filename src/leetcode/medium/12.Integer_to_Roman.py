class Solution:
    def intToRoman(self, num: int) -> str:
        storage = {
            1: "I",
            5: "V",
            10: "X",
            50: "L",
            100: "C",
            500: "D",
            1000: "M"
        }
        result = ""
        special_case_check = [100, 10, 1]
        for elem in list(storage.keys())[::-1]:
            for variant in special_case_check:
                digit = num // variant
                if digit == 4 or digit == 9:
                    result += storage.get(variant)
                    result += storage.get(digit*variant+variant)
                    num -= digit * variant
            digit = num // elem
            result += digit * storage.get(elem)
            num -= digit * elem
        return result


print(Solution().intToRoman(3749))
# "MMMDCCXLIX"