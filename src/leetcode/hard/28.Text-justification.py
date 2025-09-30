class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        result = []
        curr_line, i = [], 0
        width = 0
        while i < len(words):
            if len(words[i]) + width + len(curr_line) > maxWidth:
                if len(curr_line) == 1:
                    result.append(curr_line[0] + " " * (maxWidth-len(curr_line[0])))
                else:
                    extra_space = maxWidth - width
                    equal_space = extra_space // max(1, (len(curr_line) - 1))
                    additional_space = extra_space % max(1, (len(curr_line) - 1))
                    interim_result = ""
                    for j in range(len(curr_line)-1):
                        interim_result += curr_line[j]
                        interim_result += " " * equal_space
                        if additional_space:
                            interim_result += " "
                            additional_space -= 1
                    interim_result += curr_line[-1]
                    result.append(interim_result)

                width = 0
                curr_line = []

            curr_line.append(words[i])
            width += len(words[i])
            i += 1

        last_line = " ".join(curr_line)
        extra_spaces = maxWidth - len(last_line)
        last_line += " " * extra_spaces
        result.append(last_line)

        return result




words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16

[
   "This    is    an",
   "example  of text",
   "justification.  "
]

print(Solution().fullJustify(words, maxWidth))