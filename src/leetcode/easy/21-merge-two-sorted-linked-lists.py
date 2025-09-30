# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        result = ListNode()
        out = result
        while list1 and list2:
            if list1.val > list2.val:
                out.next = list2
                out = out.next
                list2 = list2.next
            elif list2.val >= list1.val:
                out.next = list1
                out = out.next
                list1 = list1.next
        if list1:
            out.next = list1
        if list2:
            out.next = list2
        return result.next


list1 = ListNode(5, next=ListNode(val=7, next=ListNode(val=9)))
list2 = ListNode(3)

Solution().mergeTwoLists(list1=list1, list2=list2)