class ListNode:
    def __init__(self, key, value):
        self.key, self.value = key, value
        self.prev, self.next = None, None

class LRUCache:

    def __init__(self, capacity: int):
        self.storage = dict()
        self.capacity = capacity
        self.lru = ListNode(0)
        self.mru = ListNode(0)
        self.lru.next = self.lru.prev = self.mru
        self.mru.next = self.mru.prev = self.lru

    def insert_node(self, node):
        prev_mru_node = self.mru.prev
        self.mru.prev = node
        prev_mru_node.next = node
        node.prev = prev_mru_node
        node.next = self.mru

    def remove_node(self, node):
        prev_node, next_node = node.prev, node.next
        prev_node.next, next_node.prev = next_node, prev_node


    def get(self, key: int) -> int:
        if key in self.storage:
            node = self.storage.get(key)
            # uodate lru and mru pointers
            self.remove_node(node)
            self.insert_node(node)
            return self.storage.get(key).value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.storage:
            self.remove_node(self.storage[key])
        node = ListNode(key=key, value=value)
        self.storage[key] = node
        self.insert_node(node)
        if len(self.storage) > self.capacity:
            lru_curr = self.lru.next
            self.remove_node(lru_curr)
            del self.storage[lru_curr.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)