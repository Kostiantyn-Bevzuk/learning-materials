# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        start = 0
        end = len(nums)-1


        def dfs(start, end):
            if start > end:
                return
            mid_index = (start+end) // 2
            node = TreeNode(nums[mid_index])
            node.left = dfs(start, mid_index-1)
            node.right = dfs(mid_index+1, end)
            return node

        if not nums:
            return
        return dfs(start, end)
    
"""
[-10,-3,3,0,5,9,6]
0, 6 -> mid = 3
0 -> [-10, -3, 3]
0, 2 -> mid = -3
4, 6
"""
