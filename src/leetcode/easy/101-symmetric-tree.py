# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: [TreeNode]) -> bool:
        if not root:
            return True
        return self.dfs(root.left, root.right)
    
    def dfs(self, left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return ((right.val == left.val) and self.dfs(left.left, right.right) and self.dfs(left.right, right.left))


class Solution:
    def isSymmetric(self, root: [TreeNode]) -> bool:
        from collections import deque
        if not root:
            return True
        queue = deque([root.left, root.right])
        while queue:
            left, right = queue.popleft(), queue.pop()
            if left and right and left.value == right.value:
                queue.appendleft(left.left)
                queue.appendleft(left.right)
                queue.append(right.left)
                queue.append(right.right)
            if not left and not right:
                continue
            if not left or not right:
                return False
            if left and right and left.value != right.value:
                return False
        return True