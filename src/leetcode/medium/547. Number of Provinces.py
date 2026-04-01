isConnected = [[1,1,0],[1,1,0],[0,0,1]]


class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        num_verices = len(isConnected[0])
        disjoint_set = UnionFind(num_verices)
        for i in range(len(isConnected)):
            for j in range(num_verices):
                if i == j or isConnected[i][j] == 0:
                    continue
                else:
                    disjoint_set.union(i, j)
        ans = set()
        for i in range(num_verices):
            root_value = disjoint_set.find(i)
            ans.add(root_value)

        return len(ans)



class UnionFind:
    def __init__(self, num_vertices: int):
        self.root = [i for i in range(num_vertices)]
        self.rank = [1 for _ in range(num_vertices)]

    def find(self, x: int):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x: int, y: int):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            # find rank
            if self.rank[root_x] > self.rank[root_y]:
                self.root[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.root[root_x] = root_y
            else:
                self.root[root_x] = root_y
                self.rank[root_y] += 1

    def find_connected(self, x, y):
        return self.find(x) == self.find(y)