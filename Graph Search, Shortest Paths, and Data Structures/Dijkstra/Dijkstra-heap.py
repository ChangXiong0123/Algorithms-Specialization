import min_heap
from collections import defaultdict
import os
os.chdir('Graph Search, Shortest Paths, and Data Structures/Dijkstra')


class Graph(min_heap.MinHeap):
    def __init__(self) -> None:
        self.graph = defaultdict(list)
        self.distance = {}
        # #min_heap.MinHeap.__init__(self)
        # super init to inherit all the parent properties and methods
        super().__init__()

    def read_graph(self, file):
        with open(file) as f:
            for line in f:
                t = line.rstrip().split()
                node = int(t[0])
                edges_dist = [[int(x.split(',')[0]),
                               int(x.split(',')[1])]
                              for x in t[1:]]
                self.graph[node] = edges_dist
                self.distance = {vertex: float('inf') for vertex in self.graph}
        return self.graph

# keep two invariants
# 1. elements in heap is the vertices of V-X
# 2. key[v] = the smallest Dijkstra greedy store of an
#    edge(u,v) in E with v in X

    def update_distance(self, start_node=1):
        self.distance[start_node] = 0
        # heap -- store V-X
        self.heap = [(0, start_node)]

        while len(self.heap) > 0:
            current_dist, current_node = self.extracMin()
            # Nodes can get added to the priority queue multiple times. We only
            # process a vertex the first time we remove it from the priority queue.
            if current_dist > self.distance[current_node]:
                continue

            for neigbour, weight in self.graph[current_node]:
                dist = current_dist + weight

                if dist < self.distance[neigbour]:
                    self.distance[neigbour] = dist
                    self.insertKey((dist, neigbour))


test = Graph()
test.read_graph('dijkstraData.txt')
test.update_distance()
print(test.distance)
