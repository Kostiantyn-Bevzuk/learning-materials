import heapq

class Solution:
    def kSmallestPairs(self, nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
        if not nums1 or not nums2:
            return
        min_heap = [(nums1[0]+nums2[0], 0, 0)]
        visited = set((0, 0))
        result = []
        heapq.heapify(min_heap)
        while min_heap and len(result) < k:
            _, u, v = heapq.heappop(min_heap)
            result.append([nums1[u], nums2[v]])
            if u+1 < len(nums1) and (u+1, v) not in visited:
                heapq.heappush(min_heap, (nums1[u+1] + nums2[v], u+1, v))
                visited.add((u+1, v))
            if v+1 < len(nums2) and (u, v+1) not in visited:
                heapq.heappush(min_heap, (nums1[u] + nums2[v+1], u, v+1))
                visited.add((u, v+1))
    
        return result

            

nums1 = [1,4,11]
nums2 = [2,4,6]
k=3

Solution().kSmallestPairs(nums1, nums2, k)