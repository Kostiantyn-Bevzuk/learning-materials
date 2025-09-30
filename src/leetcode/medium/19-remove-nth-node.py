# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        list_len = 0
        curr = head
        while curr:
            list_len += 1
            curr = curr.next
        dummy = ListNode(0, head)
        out = dummy
        if list_len == 1:
            return []
        for _ in range(list_len-n):
            out = out.next
        if out.next and out.next.next:
            out.next = out.next.next
            return dummy.next
        else:
            out.next = None
            return dummy.next
    
# Smarter solution

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy_node = ListNode(0, head)
        first_pointer = dummy_node
        curr = head
        for _ in range(n):
            if curr.next:
                curr = curr.next
            else:
                return None
        while curr:
            first_pointer = first_pointer.next
            curr = curr.next
        
        first_pointer.next = curr
        return dummy_node.next

[1, 2, 3, 4, 5]
n=2


[1, 2]
n=1