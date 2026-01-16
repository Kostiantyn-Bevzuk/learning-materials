import heapq

class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        heapq.heapify(self.min_heap) # more than median
        heapq.heapify(self.max_heap) # less than median

    def addNum(self, num: int) -> None:
        if len(self.min_heap) == 0:
            heapq.heappush(self.min_heap, num)
            return
        if num >= self.min_heap[0]:
            heapq.heappush(self.min_heap, num)
            self.rebalance()
        else:
            heapq.heappush(self.max_heap, -num)
            self.rebalance()

    def rebalance(self):
        if abs(len(self.min_heap) - len(self.max_heap)) < 2:
            return
        if len(self.min_heap) > len(self.max_heap):
            elem = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -elem)
        else:
            elem = heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, -elem)


    def findMedian(self) -> float:
        min_heap_len = len(self.min_heap)
        max_heap_len = len(self.max_heap)
        if (min_heap_len + max_heap_len) % 2 == 1:
            if min_heap_len > max_heap_len:
                return self.min_heap[0]
            else:
                return -self.max_heap[0]
        else:
            return (self.min_heap[0] - self.max_heap[0]) / 2



# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum(7)
obj.addNum(2)
param_2 = obj.findMedian()
obj.addNum(1)
param_2 = obj.findMedian()