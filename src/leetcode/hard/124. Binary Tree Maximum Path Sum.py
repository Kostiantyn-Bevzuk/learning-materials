# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: list[TreeNode]) -> int:
        result = [root.val]

        def dfs(root):
            if not root:
                return -1

            max_left = dfs(root.left)  # None
            max_right = dfs(root.right)  # None
            max_left = max(max_left, 0)
            max_right = max(max_right, 0)

            result[0] = max(result[0], root.val + max_left + max_right)

            return root.val + max(max_left, max_right)

        dfs(root)
        return result[0]

n4 = TreeNode(4)
n8 = TreeNode(8)
n6 = TreeNode(6)
n7 = TreeNode(7)

# middle layer
n5 = TreeNode(5, right=n8)       # if 8 should be the right child, use right=n8 instead
n2 = TreeNode(2, left=n4, right=n5)
n3 = TreeNode(3, left=n6, right=n7)

# root
root = TreeNode(1, left=n2, right=n3)

Solution().maxPathSum(root)