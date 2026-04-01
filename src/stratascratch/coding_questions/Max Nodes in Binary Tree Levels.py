from collections import deque

def find_max_nodes_per_level(tree_values):
    """
    :type tree_values: List
    :rtype: List[int]
    """
    if not tree_values:
        return []
    root = build_binary_tree(0, tree_values)
    queue = deque([root])
    result = []
    while queue:
        layer = len(queue)
        layer_max_value = -float("inf")
        for i in range(layer):
            curr_node = queue.popleft()
            if curr_node.left:
                queue.append(curr_node.left)
            if curr_node.right:
                queue.append(curr_node.right)
            if curr_node.val:
                layer_max_value = max(layer_max_value, curr_node.val)
        if layer_max_value == -float("inf"):
            result.append(None)
        else:
            result.append(layer_max_value)
    return result

class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_binary_tree(index, nums):
    if index >= len(nums):
        return None
    if nums[index] is None:
        return None
    return TreeNode(val = nums[index], left=build_binary_tree(2*index + 1), right=build_binary_tree(2*index+2))