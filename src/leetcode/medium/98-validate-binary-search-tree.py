class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: [TreeNode]) -> bool:
        prev_val = float("-inf")
        stack = []
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            if curr.val <= prev_val:
                return False
            prev_val = curr.val
            curr = curr.right
        return True


n7 = TreeNode(1)
n4 = TreeNode(2, left=n7)
# middle layer
n5 = TreeNode(4)       # if 8 should be the right child, use right=n8 instead
n2 = TreeNode(3, left=n4, right=n5)
n3 = TreeNode(6, left=None, right=None)

# root
root = TreeNode(5, left=n2, right=n3)

Solution().isValidBST(root)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: [TreeNode]) -> bool:
        self.prev = -float("inf")

        def inorder_check(root) -> bool:
            if not root:
                return True

            if not inorder_check(root.left):
                return False
            if root.val <= self.prev:
                return False
            self.prev = root.val
            if not inorder_check(root.right):
                return False
            
            return True
        
        return inorder_check(root)


n4 = TreeNode(2)
n5 = TreeNode(2)
root = TreeNode(2, left=n4, right=n5)
Solution().isValidBST(root)