# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, nxt: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.nxt = nxt

# Base BFS
# O(n) - memory and time complexity

from collections import deque

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        queue = deque([root])
        while queue:
            for indx in range(len(queue)-1):
                node = queue.popleft()
                nxt_node = queue[indx+1]
                if nxt_node:
                    node.nxt = nxt_node
                    queue.appendleft(nxt_node)
                else:
                    node.nxt = None
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            last_node = queue.popleft()
            last_node.nxt = None
            if last_node.left:
                queue.append(last_node.left)
            if last_node.right:
                queue.append(last_node.right)
            
        return root

# DFS O(n) - space and time


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        curr = root
        while curr:
            dummy = prev = Node(0)

            while curr:
                if curr.left:
                    prev.next = curr.left
                    prev = prev.next
                if curr.right:
                    prev.next = curr.right
                    prev = prev.next

                curr = curr.next

            # Go to the level below
            curr = dummy.next
        return root
