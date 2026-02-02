def linked_list_operations(elements):
    """ 
        :type elements: List[Any]
        :rtype: List[Any]
    """
    ll = LinkedList()
    ll.build(elements)
    ll.delete_first()
    ll.delete_first()
    return ll.recreate_list()
    

class Node:
    def __init__(self, val=None, next_node=None):
        self.val = val
        self.next = next_node


class LinkedList:
    def __init__(self):
        self.tail = self.head = Node()

    def build(self, elements: list):
        for elem in elements:
            self.tail.next = Node(val=elem)
            self.tail = self.tail.next
        self.head = self.head.next

    def delete_first(self):
        if not self.head:
            return
        self.head = self.head.next

    def delete_second(self):
        if not self.head or not self.head.next:
            return
        self.head.next = self.head.next.next

    def recreate_list(self) -> list:
        out = []
        pointer = self.head
        while pointer:
            out.append(pointer.val)
            pointer = pointer.next
        return out


linked_list_operations([99, 99, 88, 77, 88, 66, 99, 55])