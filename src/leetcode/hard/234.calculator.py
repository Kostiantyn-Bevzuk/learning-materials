class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        operations_stack = []
        operations = {
            "+": lambda x, y: x+y,
            "-": lambda x, y: x-y
        }
        reverse_mapping = {
            "-": "+",
            "+": "-"
        }
        non_digits = ["(", ")", "+", "-", " "]
        indx = 0
        is_plus = True
        resolved_s = ""
        curr_digit = ""
        while indx < len(s):
            if s[indx] == "(" and indx > 0:
                if s[indx-1] == "-":
                    is_plus=False
                    curr_digit = "-"
                    while s[indx+1] not in non_digits:
                        curr_digit += f"{s[indx+1]}"
                        indx += 1
                    
                indx += 1
                while s[indx] != ")":
                    if s[indx] in operations:
                        resolved_s += s[indx] if is_plus else reverse_mapping[s[indx]]
                    elif s[indx] not in non_digits:
                        resolved_s += s[indx]
                    indx += 1
            elif s[indx] not in non_digits:
                resolved_s += s[indx]
            elif s[indx] == "-" and s[indx+1] == "(":
                continue
            elif s[indx] in operations: # -( /   +( / - / +
                resolved_s += s[indx]
            indx += 1
        return eval(resolved_s)
        # if resolved_s[0] == "-":
        #     stack.append(int(resolved_s[:2]))
        #     resolved_s = resolved_s[2:]
        # for indx in range(len(resolved_s)):
        #     if resolved_s[indx] in operations:
        #         operations_stack.append(resolved_s[indx])
        #     elif resolved_s[indx] not in operations:
        #         if operations_stack:
        #             last_op = operations_stack.pop()
        #             last_val = stack.pop()
        #             stack.append(operations[last_op](last_val, int(resolved_s[indx])))
        #         else:
        #             stack.append(int(resolved_s[indx]))
        return stack[-1]

print(Solution().calculate("(1+(4+5+2)-3)+(6+8)"))
