from collections import deque

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        mapper = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        queue = deque(mapper[digits[0]]) # a, b, c
        index = 1
        while index < len(digits):
            for _ in range(len(queue)):
                curr_char = queue.popleft()
                for char in mapper[digits[index]]:
                    queue.append(curr_char+char)
            index += 1
        return [elem for elem in queue]
    

# Alternative


class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        mapper = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        stack = [(0, "")] # -> [(1, "a"), (1, "b")]
        result = []
        while stack:
            curr_indx, curr_comb = stack.pop()
            if curr_indx == len(digits):
                result.append(curr_comb)
            else:
                for letter in mapper[digits[curr_indx]]:
                    stack.append((curr_indx+1, curr_comb + letter))

        return result

# Recursion

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        mapper = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        result = []
        def backtrack(index, curr_str):
            if index == len(digits):
                result.append(curr_str)
                return

            for c in mapper[digits[index]]:
                backtrack(index+1, curr_str+c)
        if not digits:
            return []
        backtrack(0, "")
        return result
