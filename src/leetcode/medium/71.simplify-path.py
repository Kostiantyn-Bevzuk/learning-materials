class Solution:
    def simplifyPath(self, path: str) -> str:
        result = []
        current_word = ""
        for char in path[1:]:
            if char != "/":
                current_word += char
                continue
            else:
                if not current_word:
                    continue
                elif current_word == ".":
                    current_word = ""
                    continue
                elif current_word == "..":
                    if result:
                        result.pop()
                else:
                    result.append(current_word)
                current_word = ""
        if current_word == ".":
            return "/" + "/".join(result)
        elif current_word == "..":
            if result:
                result.pop()
        elif current_word:
            result.append(current_word)
        return "/" + "/".join(result)


path = "/.../a/../b/c/../d/./"
Solution().simplifyPath(path)