# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def build_in_order_list(root):
            if not root:
                return []
            return build_in_order_list(root.left) + [root.val] + build_in_order_list(root.right)

        def find_two_swapped_values(arr: list[int]) -> tuple[int, int]:
            first, second = None, None
            for i in range(1, len(arr)):
                if arr[i-1] > arr[i]:
                    if first:
                        second = arr[i]
                        return first, second
                    first = arr[i-1]
                    second = arr[i]

            return first, second

        def swap_values(root, counter):
            if root:
                if root.val == f or root.val == s:
                    root.val = s if root.val == f else f
                    counter -= 1
                if counter:
                    swap_values(root.left, counter)
                    swap_values(root.right, counter)

        arr = build_in_order_list(root)
        f, s = find_two_swapped_values(arr)
        swap_values(root, 2)


# [1, 3, 2] -> [1, 2, 3]
# [4, 2, 3, 1] -> [1, 2, 3, 4]

# DFS
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        self.first = self.second = None
        self.prev = -float("inf")
        def dfs(root):
            if not root:
                return

            dfs(root.left)
            if self.prev.val > root.val:
                if self.first:
                    self.second = root.val
                self.first = self.prev
                self.second = root
            self.prev = root
            dfs(root.right)

        dfs(root)
        self.first, self.second = self.second, self.first

#  [1]
# [2, 3]