class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        # Sliding window is not useful here
        storage = {0: 1}
        res = 0
        currsum = 0
        for elem in nums:
            currsum += elem
            diff = currsum - k
            res += storage.get(diff, 0)
            storage[currsum] = storage.get(currsum, 0) + 1
        return res

print(Solution().subarraySum([1,1,-1, 1, 1, 1], 3))
[1,1,1]
[1, 2, 3]