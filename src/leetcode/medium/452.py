# class Solution:
#     def findMinArrowShots(self, points: list[list[int]]) -> int:
#         if not points:
#             return 0
#         points.sort(key=lambda x: x[0])
#         result = [points[0]]
#         for start, end in points[1:]:
#             curr_inter = result[-1]
#             if start >= curr_inter[0] and start <= curr_inter[1]:
#                 result[-1] = [
#                     max(start, curr_inter[0]), 
#                     min(end, curr_inter[1])
#                     ]
#             else:
#                 result.append([start, end])
#         return len(result)

class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort(key=lambda x: x[0])
        curr_inter = points[0]
        result = len(points)
        for start, end in points[1:]:
            if start >= curr_inter[0] and start <= curr_inter[1]:
                curr_inter = [
                    max(start, curr_inter[0]), 
                    min(end, curr_inter[1])
                    ]
                result -= 1
            else:
                curr_inter = [start, end]
        return result