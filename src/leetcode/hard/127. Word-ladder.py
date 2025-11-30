from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        number_transform = 1
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        queue = deque()
        queue.append(beginWord)
        wordSet = set(wordList)
        if beginWord in wordSet:
            wordSet.remove(beginWord)
        if endWord not in wordSet:
            return 0

        while queue:
            number_transform += 1
            for _ in range(len(queue)): # layer of bfs
                elem = queue.popleft()
                for indx in range(len(elem)):
                    elemList = list(elem)
                    for char in alphabet:
                        if char == elemList[indx]:
                            continue
                        elemList[indx] = char
                        if (possible_word := "".join(elemList)) in wordSet:
                            if possible_word == endWord:
                                return number_transform
                            queue.append(possible_word)
                            wordSet.remove(possible_word)
        return 0

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

Solution().ladderLength(beginWord, endWord, wordList)

