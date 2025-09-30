# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


    # Count nodes recursively left subtree nodes and right sub tree
    # using completness property of binary tree. We can achieve
    # this by checking left hight of subtree and most right hight of subtree
    # if it is matched -> we return (heigh of current subtree * 2) - 1
    # if not we return 1 + count_of_nodes(left_side) + count_of_nodes(right_side)
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        return self.count_of_nodes(root)
    def count_of_nodes(self, node):
        if not node:
            return 0
        ptr1 = ptr2 = node
        left_height = 1
        right_height = 1
        while ptr1.left:
            left_height += 1
            ptr1 = ptr1.left
        while ptr2.right:
            right_height += 1
            ptr2 = ptr2.right
        if left_height == right_height:
            return 2**left_height - 1
        else:
            return 1 + self.count_of_nodes(node.left) + self.count_of_nodes(node.right)
