# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flatten(self, root: [TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def dfs(root):
            if not root:
                return None
            
            leftTail = dfs(root.left)
            rightTail = dfs(root.right)

            if root.left:
                leftTail.right = root.right
                root.right = root.left
                root.left = None

            if rightTail:
                return rightTail
            elif leftTail:
                return leftTail
            else:
                return root
        
        dfs(root)

root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(5)
root1.left.left = TreeNode(3)
root1.left.right = TreeNode(4)
root1.right.right = TreeNode(6)


Solution().flatten(root=root1)