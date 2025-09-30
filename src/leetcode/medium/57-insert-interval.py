class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        result = []
        for indx in range(len(intervals)):
            if newInterval[1] < intervals[indx][0]:
                result.append(newInterval)
                return result + intervals[indx:]
            elif newInterval[0] > intervals[indx][1]:
                result.append(intervals[indx])

            # is overlapping
            else:
                newInterval = [
                    min(newInterval[0], intervals[indx][0]),
                    max(newInterval[1], intervals[indx][1])
                    ]
        result.append(newInterval)
        return result




# if new_inter[0] < current_pos[1] and new_inter -> merge
# if new_inter[0] < curr_pos[0] -> insert

intervals = [[2,3], [9, 10], [11,12]]
newInterval = [11, 13]
 
print(Solution().insert(intervals, newInterval))


