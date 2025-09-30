# # Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# class Solution:
#     def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
#         curr_ptr = 0
#         storage = []
#         empty_node = ListNode()
#         result = empty_node
#         curr_head = head

#         while curr_ptr < left-1:
#             result.next = curr_head
#             result = result.next
#             curr_ptr += 1
#             curr_head = curr_head.next

#         while left-1 <= curr_ptr <= right-1 and curr_head:
#             storage.append(curr_head.val)
#             curr_ptr += 1
#             curr_head = curr_head.next

#         while storage:
#             val = storage.pop()
#             result.next = ListNode(val)
#             result = result.next

#         while curr_head:
#             result.next = curr_head
#             result = result.next
#             curr_head = curr_head.next

#         return empty_node.next


# Alternative
# O(n) - time; O(1) - space

class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        dummy = ListNode(None, head)
        left_prev, curr = dummy, head


        for i in range(left-1):
            left_prev, curr = curr, curr.next
        
        prev = None
        for i in range(right-left+1):
            tmp_node = curr.next
            curr.next = prev
            prev, curr = curr, tmp_node

        left_prev.next.next = curr
        left_prev.next = prev

        return dummy.next
