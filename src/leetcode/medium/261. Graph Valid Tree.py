class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        disjoint_set = UnionFind(n)
        components_added = 0
        for edge in edges:
            vertex_1, vertex_2 = edge
            if disjoint_set.find(vertex_1) != disjoint_set.find(vertex_2):
                disjoint_set.union(vertex_1, vertex_2)
                components_added += 1
            else:
                #cycle
                return False
        return components_added == n-1


class UnionFind:
    def __init__(self, num_vertices: int):
        self.root = [i for i in range(num_vertices)]
        self.rank = [1 for _ in range(num_vertices)]

    def find(self, x: int) -> int:
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x: int, y: int):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.root[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.root[root_x] = root_y
            else:
                self.root[root_x] = root_y
                self.rank[root_y] += 1
        
    def compare(self, x, y):
        return self.find(x) == self.find(y)
    
