# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbour: list = None):
        self.val = val
        self.neighbour = neighbour if neighbour is not None else []

from typing import Optional
# DFS
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        old_to_new = dict()
        if not node:
            return None

        def dfs(node):
            if node in old_to_new:
                return old_to_new[node]

            copy = Node(node.val)
            old_to_new[node] = copy

            for neighbour in node.neighbors:
                copy.neighbors.append(dfs(neighbour))

            return copy

        return dfs(node)

# BFS
from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        queue = deque([node])
        clone = Node(node.val)
        old_to_new = {node: clone}

        while queue:
            curr_node = queue.popleft()
            clone_node = old_to_new[curr_node]
            for neighbor in curr_node.neighbour:
                if neighbor not in old_to_new:
                    old_to_new[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                clone_node.neighbors.append(old_to_new[neighbor])

        return clone
    
        

