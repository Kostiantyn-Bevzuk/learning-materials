class Trie:

    def __init__(self):
        self.storage = dict()
        self.state_alias = "end_of_word_state"

    def insert(self, word: str) -> None:
        tmp_layer = self.storage
        word_length = len(word)
        for index in range(word_length):
            if (char:=word[index]) not in tmp_layer:
                tmp_layer[char] = {self.state_alias: False}
            if index == word_length-1:
                tmp_layer[char][self.state_alias] = True
            tmp_layer = tmp_layer.get(char)


    def search(self, word: str) -> bool:
        tmp_layer = self.storage
        for char in word:
            if char in tmp_layer:
                tmp_layer = tmp_layer[char]
            else:
                return False
        return tmp_layer.get(self.state_alias)

    def startsWith(self, prefix: str) -> bool:
        tmp_layer = self.storage
        for char in prefix:
            if char not in tmp_layer:
                return False
            tmp_layer = tmp_layer[char]
        return True
"""
{
    "c": {""}
    "a": (["r"], is_end_of_word: bool)
    "r": (["d"], is_end_of_word: bool)
}
"""

# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert("car")
obj.insert("card")
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)