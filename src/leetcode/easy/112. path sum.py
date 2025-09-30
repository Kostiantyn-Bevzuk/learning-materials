class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: [TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        targetSum -= root.val
        if not root.left and not root.right:
            return targetSum == 1
        
        if root.left:
            if self.hasPathSum(root.left, targetSum):
                return True
        if root.right:
           if self.hasPathSum(root.right, targetSum):
               return True

        return False
    

root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(5)
root1.left.left = TreeNode(3)
root1.left.right = TreeNode(4)
root1.right.right = TreeNode(6)


Solution().hasPathSum(root=root1, targetSum=6)

