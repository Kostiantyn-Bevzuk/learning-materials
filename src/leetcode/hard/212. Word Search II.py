# Alternative of Trie implementation


class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word: bool = False

    def add_word(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.end_of_word = True


class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        root = TrieNode()
        for w in words:
            root.add_word(w)
        board_rows = len(board)
        board_cols = len(board[0])
        result, visited = set(), set()

        def dfs(row, col, node: TrieNode, word: str):
            if (
                row < 0
                or col < 0
                or row == board_rows
                or col == board_cols
                or (row, col) in visited
                or board[row][col] not in node.children
            ):
                return

            visited.add((row, col))
            char = board[row][col]
            word += char
            node = node.children[char]
            if node.end_of_word:
                result.add(word)

            for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_row = row + direction[0]
                new_col = col + direction[1]
                dfs(new_row, new_col, node, word)

            visited.remove((row, col))


        for row in range(board_rows):
            for col in range(board_cols):
                dfs(row, col, root, "")

        return list(result)