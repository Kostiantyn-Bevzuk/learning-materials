# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        prio_queue = []                  # just a list
        heapq.heapify(prio_queue)
        dummy = head = ListNode()
        for i, list_head in enumerate(lists):
            if list_head:
                heapq.heappush(prio_queue, (list_head.val, i, list_head))
        while prio_queue:
            _, i, curr_min_head = heapq.heappop(prio_queue)
            head.next = curr_min_head
            head = head.next
            if curr_min_head.next:
                heapq.heappush(prio_queue, (curr_min_head.next.val, i, curr_min_head.next))
        
        return dummy.next

                
        # return dummy.next
    
# O(k) where k - len listl n len linked list - space
# N*log(k) - time complexity, N - overall number of elems