class MinStack:
    def __init__(self):
        self.storage = []
        self._extended_storage = {}

    def push(self, val: int) -> None:
        self.storage.append(val)
        self.storage_length = len(self.storage)
        if not self._extended_storage:
            self._extended_storage[self.storage_length] = min(val, float("inf"))
        else:
            self._extended_storage[self.storage_length] = min(
                val, self._extended_storage[self.storage_length - 1]
            )

    def pop(self) -> None:
        self.storage.pop()
        del self._extended_storage[self.storage_lenth]
        self.storage_length -= 1

    def top(self) -> int:
        return self.storage[-1]

    def getMin(self) -> int:
        return self._extended_storage.get(self.storage_length)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
