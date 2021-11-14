from collections import defaultdict


class Graph:
    def __init__(self) -> None:
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def BFS(self, s):
        # s is the initialized vertex
        visited = set()
        # Create a queue for BFS
        queue = []

        # mark source node s as visited
        queue.append(s)
        visited.add(s)

        while queue:
            v = queue.pop(0)
            print(v)
            for neigbours in self.graph[v]:
                if neigbours not in visited:
                    visited.add(neigbours)
                    queue.append(neigbours)


g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print("Following is Breadth First Traversal"
      " (starting from vertex 2)")
g.BFS(2)
