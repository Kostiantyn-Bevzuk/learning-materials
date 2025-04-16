class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        mapping = {}
        res = float("inf")
        for i, val in enumerate(cards):
            if val not in mapping:
                mapping[val] = i
            else:
                res = min(res, i - mapping.get(val) + 1)
                mapping[val] = i
        return -1 if res == float("inf") else res