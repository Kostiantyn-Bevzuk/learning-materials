import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: list[int], capital: list[int]) -> int:
        max_heap = []
        heapq.heapify(max_heap)
        min_heap = [(c, p) for c, p in zip(capital, profits)]
        heapq.heapify(min_heap)

        while k > 0:
            while min_heap and min_heap[0][0] <= w:
                curr_min_capital, curr_min_profit = heapq.heappop(min_heap)
                heapq.heappush(max_heap, (-curr_min_profit, curr_min_capital))
            if not max_heap:
                break
            curr_profit, _ = heapq.heappop(max_heap)
            w -= curr_profit
            k -= 1
        return w

