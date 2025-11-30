# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: [ListNode]) -> [ListNode]:
        # split
        if not head or not head.next:
            return head
        left = head
        right = self.get_mid(head) # function get mid will get middle linked list node
        tmp = right.next
        right.next = None # it works because we cut linked list(add comment to obsidian on this)
        right = tmp

        left = self.sortList(left)
        right = self.sortList(right)

        return self.merge(left, right)

    def get_mid(self, node):
        slow, fast = node, node.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
    
    def merge(self, left_list, right_list):
        dummy = head = ListNode()
        while left_list and right_list:
            if left_list.val >= right_list.val:
                head.next = right_list
                right_list = right_list.next
            elif right_list.val > left_list.val:
                head.next = left_list
                left_list = left_list.next
            head = head.next
        if left_list:
            head.next = left_list
        if right_list:
            head.next = right_list
        return dummy.next

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Helper functions for testing
def build_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def to_array(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

def print_list(head):
    print(" -> ".join(map(str, to_array(head))) + " -> None")


# Create your test linked list
head = build_list([4, 2, 1, 3])

# Verify
print_list(head)  # Output: 4 -> 2 -> 1 -> 3 -> None

# Test your solution
# result = your_function(head)
# print(to_array(result))

head = build_list([4, 2, 1, 3])

Solution().sortList(head)