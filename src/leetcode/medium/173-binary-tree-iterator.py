# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        self.dfs(root)

    def next(self) -> int:
        return self.stack.pop(0)

    def hasNext(self) -> bool:
        return len(self.stack) > 0

    def dfs(self, root):
        if not root:
            return
        if root.left:
            self.dfs(root.left)
        self.stack.append(root.val)
        if root.right:
            self.dfs(root.right)
        


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        self.dfs(root)

    def next(self) -> int:
        node = self.stack.pop(-1)
        self.dfs(node.right)
        return node.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0

    def dfs(self, root):
        if root:
            self.stack.append(root)
            self.dfs(root.left)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()