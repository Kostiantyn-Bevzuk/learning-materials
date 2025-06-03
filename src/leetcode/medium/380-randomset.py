class RandomizedSet:

    def __init__(self):
        self.hashmap = {} # {0: 0} value 0 with index
        self.index_list = [] # [1, 3, 4]

    def insert(self, val: int) -> bool:
        if val not in self.hashmap:
            self.hashmap[val] = len(self.index_list)
            self.index_list.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.hashmap:
            index = self.hashmap.get(val)
            last_val = self.index_list[-1]
            self.index_list[index] = last_val
            self.index_list.pop()
            self.hashmap[last_val] = index
            del self.hashmap[val]
            return True
        return False


    def getRandom(self) -> int:
        import random
        return random.choice(self.index_list)
        

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# print(obj.remove(0))
# print(obj.remove(0))
# print(obj.insert(0))
# print(obj.getRandom())
# print(obj.remove(0))
# print(obj.insert(0))
# print(obj.insert(1))
# print(obj.remove(2))
# print(obj.insert(2))
# print(obj.getRandom())
# print(obj.remove(1))
# print(obj.insert(2))
# print(obj.getRandom())