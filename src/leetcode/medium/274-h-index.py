class Solution:
    def hIndex(self, citations: list[int]) -> int:
        n = len(citations)
        storage = [0] * (n+1)
        for i in range(n):
            storage[min(citations[i], len(storage)-1)] += 1

        h = n
        summ = 0
        while h > 0:
            summ += storage[h]
            if summ >= h:
                return h
            h -= 1
        return h


citations = [1,3,1]
[0, 2, 0, 1]
# citations = [3,0,6,1,5]

print(Solution().hIndex(citations))

[0, 1, 3, 5, 9]
[1, 1, 0, 1, 0, 2]