class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    leaf_sum = 0
    curr_number = ""
    def sumNumbers(self, root: [TreeNode]) -> int:
        if not root:
            return None
        curr_number = str(root.val)
        self.dfs(root.left, curr_number)
        self.dfs(root.right, curr_number)

        return self.leaf_sum
    
    def dfs(self,root, curr_number):
        curr_number += str(root.val)
        if not root.left and not root.right:
            self.leaf_sum += int(curr_number)

        if root.left:
            self.dfs(root.left, curr_number)
        if root.right:
            self.dfs(root.right, curr_number)

class Solution:
    def sumNumbers(self, root: [TreeNode]) -> int:

        def dfs(root, curr_num):
            if not root:
                return 0
            
            curr_num = curr_num * 10 + root.val

            if not root.left and not root.right:
                return curr_num

            return dfs(root.left, curr_num) + dfs(root.right, curr_num)
        
        return dfs(root, 0)


            

root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)

Solution().sumNumbers(root1)