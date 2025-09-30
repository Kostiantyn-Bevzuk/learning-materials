# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None

        if root.val == p.val or root.val == q.val:
            return root
        out_left = self.lowestCommonAncestor(root.left, p, q)
        out_right = self.lowestCommonAncestor(root.right, p, q)
        if out_left and out_right:
            return root
        elif out_left:
            return out_left
        elif out_right:
            return out_right
        



    # def dfs_subtree(self, root, p, q):
    #     if not root:
    #         return None
    #     if root.val == p.val or root.val == q.val:
    #         if self.find_first:
    #             return self.initial_node
    #         else:
    #             self.find_first = True
    #             self.initial_node = root
    #     self.dfs_subtree(root.left, p, q)
    #     if root.val == p.val or root.val == q.val:
    #         if self.find_first:
    #             return self.initial_node
    #         else:
    #             self.find_first = True
    #             self.initial_node = root
    #     self.dfs_subtree(root.right, p, q)
    #     return None
