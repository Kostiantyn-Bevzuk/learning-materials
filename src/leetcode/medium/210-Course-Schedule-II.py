from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        graph = defaultdict(list)
        for condition in prerequisites:
            graph[condition[0]].append(condition[1])

        VISITED = 2
        IN_PROGRESS = 1
        UNSEEN = 0
        states = numCourses * [UNSEEN]
        out = []

        def dfs(node):
            curr_state = states[node]
            if curr_state == IN_PROGRESS:
                return False
            if curr_state == VISITED:
                return True
            
            states[node] = IN_PROGRESS
            for neighbour in graph[node]:
                if not dfs(neighbour):
                    return False

            states[node] = VISITED
            out.append(node)

            return True

        for course in range(numCourses):
            if not dfs(course):
                return []

        return out

num_cors = 2

prere = [[1,0]]

Solution().findOrder(num_cors, prere)
