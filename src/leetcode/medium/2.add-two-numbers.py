# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        storage = 0
        curr_l1, curr_l2 = l1, l2
        new_node = ListNode()
        result = new_node
        while curr_l1 or curr_l2 or storage:
            tmp = storage
            storage = 0
            if curr_l1:
                tmp += curr_l1.val
                curr_l1 = curr_l1.next
            if curr_l2:
                tmp += curr_l2.val
                curr_l2 = curr_l2.next
            if tmp >= 10:
                storage = 1
                tmp = tmp%10
            
            result.next = ListNode(val=tmp)
            result = result.next
        return new_node.next
            
            