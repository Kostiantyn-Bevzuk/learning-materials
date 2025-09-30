# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        storage = {None:None}
        curr = head
        while curr:
            copy = Node(curr.val)
            storage[curr] = copy
            curr = curr.next

        
        curr = head
        while curr:
            copy = storage[curr]
            copy.next = storage[curr.next]
            copy.random = storage[curr.random]

        return storage[head]