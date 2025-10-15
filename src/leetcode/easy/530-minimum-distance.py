# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getMinimumDifference(self, root:[TreeNode]) -> int:
        prev_node = [None]
        min_distance = [float("inf")]


        def dfs(root):
            if not root:
                return

            dfs(root.left)

            if not prev_node[0]:
                prev_node[0] = root.val
            
        dfs(root)

root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(5)
root1.left.left = TreeNode(3)
root1.left.right = TreeNode(4)
root1.right.right = TreeNode(6)

Solution().getMinimumDifference(root1)