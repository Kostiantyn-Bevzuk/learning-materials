class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        if len(intervals) == 1:
            return intervals
        intervals.sort(key=lambda x: x[0])
        result = [intervals[0]]
        for s, e in intervals[1:]:
            last_e = result[-1][1]
            if s <= last_e:
                result[-1][1] = max(last_e, e)
            else:
                result.append([s, e])
        return result


intervals = [[2,3],[4,5],[6,7],[8,9],[1,10]]
# [8,10],[15,18]

print(Solution().merge(intervals))