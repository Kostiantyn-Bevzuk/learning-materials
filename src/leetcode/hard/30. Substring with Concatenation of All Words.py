class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        freq_map = {}
        result = []
        for word in words:
            if word in freq_map:
                freq_map[word] += 1
            else:
                freq_map[word] = 1

        word_len = len(words[0])
        for i in range(word_len):
            rolling_map = {}
            left = i
            right = i
            count = 0
            while right + word_len <= len(s):
                curr_word = s[right: right+word_len]
                right += word_len

                if curr_word in freq_map:
                    count += 1
                    if curr_word in rolling_map:
                        rolling_map[curr_word] += 1
                    else:
                        rolling_map[curr_word] = 1

                    while rolling_map[curr_word] > freq_map[curr_word]:
                        rolling_map[s[left: left+word_len]] -= 1
                        left += word_len
                        count -= 1

                    if count == len(words):
                        result.append(left)

                else:
                    rolling_map.clear()
                    count = 0
                    left = right

        return result

s = "barfoofoobarthefoobarman"
words = ["bar","foo","the"]
print(Solution().findSubstring(s=s, words=words))

