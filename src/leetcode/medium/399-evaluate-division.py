from collections import defaultdict, deque
from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        for i in range(len(equations)):
            first_node, second_node = equations[i]
            graph[first_node][second_node] = values[i]
            graph[second_node][first_node] = 1/values[i]

        output = []
        for q in queries:
            fs_node, sec_node = q
            visited_nodes = set([fs_node])
            if fs_node not in graph or sec_node not in graph:
                output.append(-1.)
                continue
            elif fs_node == sec_node:
                output.append(1.)
                continue
            queue = deque()
            queue.append((fs_node, 1))
            path_exist = False
            while queue and not path_exist:
                curr_node, product = queue.popleft()
                layer = graph[curr_node]
                for node in layer:
                    if node == sec_node:
                        output.append(product*layer[node])
                        path_exist = True
                        break
                    if node not in visited_nodes:
                        visited_nodes.add(node)
                        queue.append((node, product*layer[node]))
            if not path_exist:
                output.append(-1.)
        return output


                # if curr_node in visited_nodes:
                    
                # els
                # visited_nodes.add(curr_node)



equations = [["a","b"],["c","d"]]
values = [1.0,1.0]
queries = [["a","c"],["b","d"],["b","a"],["d","c"]]

out = Solution().calcEquation(equations, values, queries)

print(out)