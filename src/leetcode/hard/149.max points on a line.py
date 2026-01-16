from collections import defaultdict
class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        result = 1
        for i in range(len(points)):
            anchor_x, anchor_y = points[i][0], points[i][1]
            storage = defaultdict(int)
            for j in range(len(points)):
                curr_x, curr_y = points[j][0], points[j][1]
                if anchor_x == curr_x and anchor_y == curr_y:
                    continue
                if curr_x == anchor_x:
                    slope = (1, 0)
                else:
                    slope = (curr_y-anchor_y) / (curr_x-anchor_x) # TODO: normalize for ideal solution
                storage[slope] += 1
                result = max(result, storage[slope] + 1)

        return result

# y = kx + b
# k = (y2 - y1)/(x2-x1)

# (1, 4)
# (1, 2) -> inf

# (2, 3)
# (2, 8) -> inf
# becuase we fixate one point and calculate slope according to it.