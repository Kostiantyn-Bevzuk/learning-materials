import heapq

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heap = []
        heapq.heapify(heap)
        for num in nums:
            if len(heap) < k:
                heapq.heappush(heap, num)
            else:
                heapq.heappushpop(heap, num)

        return heapq.heappop()


# class Solution:
#     def findKthLargest(self, nums: list[int], k: int) -> int:
#         ...