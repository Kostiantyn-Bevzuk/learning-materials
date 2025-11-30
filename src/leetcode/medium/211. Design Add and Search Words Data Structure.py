class WordDictionary:

    def __init__(self):
        self.storage = dict()
        self.state_alias = "end_of_word_state"

    def addWord(self, word: str) -> None:
        layer = self.storage
        word_length = len(word)
        for index in range(word_length):
            if (char:=word[index]) not in layer:
                layer[char] = {self.state_alias: False}
            if index == word_length-1:
                layer[char][self.state_alias] = True
            layer = layer[char]

    def search(self, word: str) -> bool:
        def dfs(layer, index):
            char = word[index]
            if index == len(word)-1:
                if char == ".":
                    for key in layer.keys():
                        if key == self.state_alias:
                            continue
                        if layer[key][self.state_alias]:
                            return True
                    return False
                else:
                    if char in layer and layer[char][self.state_alias]:
                        return True
                    else:
                        return False
            if char == ".":  # one root
                for key in layer.keys():
                    if key == self.state_alias:
                        continue
                    if dfs(layer[key], index+1):
                        return True
                return False
            else:
                if char not in layer:
                    return False
                if not dfs(layer[char], index+1):
                    return False
                return True

        return dfs(self.storage, 0)



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)