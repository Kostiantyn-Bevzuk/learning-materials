class MyHashMap:
    def __init__(self):
        self.map = [ListNode() for _ in range(1000)]

    def hash_key(self, key: int) -> int:
        return key % len(self.map)

    def put(self, key: int, value: int) -> None:
        indx = self.hash_key(key)
        curr_pos = self.map[indx]
        while curr_pos.next_elem:
            if curr_pos.next_elem.key == key:
                curr_pos.next_elem.value = value
                return
            curr_pos = curr_pos.next_elem
        curr_pos.next_elem = ListNode(key=key, value=value)

    def get(self, key: int) -> int:
        indx = self.hash_key(key)
        curr_pos = self.map[indx]
        while curr_pos:
            if curr_pos.key == key:
                return curr_pos.value
            curr_pos = curr_pos.next_elem
        return -1

    def remove(self, key: int) -> None:
        indx = self.hash_key(key)
        curr_pos = self.map[indx]
        while curr_pos and curr_pos.next_elem:
            if curr_pos.next_elem.key == key:
                curr_pos.next_elem = curr_pos.next_elem.next_elem
                return
            curr_pos = curr_pos.next_elem


class ListNode:
    def __init__(
        self, key: int = -1, value: int = -1, next_elem=None
    ) -> None:
        self.key = key
        self.value = value
        self.next_elem = next_elem


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
