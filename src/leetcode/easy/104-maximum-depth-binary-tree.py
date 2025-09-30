# Definition for a binary tree node.

# DFS

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
            
# BFS
from collections import deque
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = 0
        queue = deque([root])
        while queue:
            res += 1
            for _ in range(len(queue)):
                elem = queue.popleft()
                if elem.left:
                    queue.append(elem.left)
                if elem.right:
                    queue.append(elem.right)
                
        return res
        
# 3 Solution BFS but as a stack
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        res = 0

        stack = [(root, 1)] # stack and depth
        while stack:
            node, depth = stack.pop()
            if node:
                stack.append((node.left, depth+1))
                stack.append((node.right, depth+1))
                res = max(res, depth)

        return res