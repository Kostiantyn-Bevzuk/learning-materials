from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for schedule in prerequisites:
            vertex_1, vertex_2 = schedule[0], schedule[1]
            graph[vertex_1].append(vertex_2)

        UNVISITED = 0
        VISITED = 2  # all good
        IN_PROGRESS = 1  # don't know yet
        STATES = numCourses * [UNVISITED]

        def dfs(vertex):
            curr_state = STATES[vertex]
            if curr_state == VISITED:
                return True
            elif curr_state == IN_PROGRESS:
                return False

            STATES[vertex] = IN_PROGRESS

            for neighbour in graph[vertex]:
                if not dfs(neighbour):
                    return False

            STATES[vertex] = VISITED
            return True

        for vertex in range(numCourses):
            if not dfs(vertex):
                return False
        return True

