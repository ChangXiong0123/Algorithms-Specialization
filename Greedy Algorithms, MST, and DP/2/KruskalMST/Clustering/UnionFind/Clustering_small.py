# Kruskal's algo and rank unionfind data structure
# max spacing clustering

from collections import defaultdict


class UnionFind:
    def __init__(self) -> None:
        self.num_of_nodes = 500
        self.parent = [-1]*(self.num_of_nodes)
        self.rank = [0]*(self.num_of_nodes)
        self.num_of_cluster = self.num_of_nodes

    def find(self, node):
        # find and path compression
        if self.parent[node] == -1:
            return node
        elif self.parent[node] != -1:
            return self.find(self.parent[node])

    def union(self, x, y):
        p_x = self.find(x)
        p_y = self.find(y)

        if p_x == p_y and p_x != -1 and p_y != -1:
            return

        self.num_of_cluster -= 1
        if self.rank[p_x] == self.rank[p_y]:
            # merge y to x
            self.parent[p_y] = p_x
            # if rank equal then parent's rank increase by 1
            self.rank[p_x] += 1

        elif self.rank[p_x] < self.rank[p_y]:
            # merge x to y and rank stay unchange
            self.parent[p_x] = p_y
        else:
            self.parent[p_y] = p_x

    def cycle_check(self, x, y):
        """check whether there is cycle  --> 
        check if leader point of x and y is the same"""
        return self.find(x) == self.find(y)


class cluster(UnionFind):
    def __init__(self) -> None:
        super().__init__()
        self.edges = []

    def read_edge(self, file):
        """read the file,
        return the edges, graph, number of nodes
        """
        with open(file) as file:
            for position, lines in enumerate(file):
                if position != 0:
                    # node1, node2, cost
                    node1, node2, cost = int(lines.split()[0])-1, int(
                        lines.split()[1])-1, int(lines.split()[2])
                    self.edges.append((node1, node2, cost))
                if position == 0:
                    self.num_of_nodes = int(lines.split()[0])
        return self.edges, self.num_of_nodes

    def clustering(self, k):
        """maximum spacing clusterings, 
        implementation with Kruskal's algo and rank unionfind data structure

        return the maximum spacing of a k-clustering
        """
        # sort edges increasingly (cost)
        self.edges.sort(key=lambda x: x[2])
        for edge in self.edges:
            if not self.cycle_check(edge[0], edge[1]) and self.num_of_cluster != k:
                self.union(edge[0], edge[1])
            if not self.cycle_check(edge[0], edge[1]) and self.num_of_cluster == k:
                return edge[2]


if __name__ == "__main__":
    c = cluster()
    c.read_edge(
        'Greedy Algorithms, MST, and DP/2/KruskalMST/Clustering/UnionFind/clustering_small.txt')
    max_space = c.clustering(k=4)
    print(max_space)
