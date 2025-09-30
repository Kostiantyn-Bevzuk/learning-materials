# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        node_counter = 0
        if not head:
            return head
        cur = head
        first_node = head
        while cur:
            node_counter += 1
            if not cur.next:
                if (k:= k % node_counter) == 0:
                    return head
                cur.next = first_node
                break
            cur = cur.next

        dummy = ListNode(None, head)
        out = dummy.next
        for _ in range(node_counter-k-1):
            out = out.next
        tmp_head = out.next
        out.next = None

        return tmp_head
