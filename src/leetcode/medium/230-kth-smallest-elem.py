# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: [TreeNode], k: int) -> int:
        vals_stack = []
        def dfs(root):
            if not root:
                return
            if root.left:
                dfs(root.left)
            if root.right:
                dfs(root.right)

        dfs(root)
        return vals_stack[k-1]
    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: [TreeNode], k: int) -> int:
        stack = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            # ----
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right
                
        

n7 = TreeNode(1)
n4 = TreeNode(2, left=n7)
# middle layer
n5 = TreeNode(4)       # if 8 should be the right child, use right=n8 instead
n2 = TreeNode(3, left=n4, right=n5)
n3 = TreeNode(6, left=None, right=None)

# root
root = TreeNode(5, left=n2, right=n3)

Solution().kthSmallest(root, 3)