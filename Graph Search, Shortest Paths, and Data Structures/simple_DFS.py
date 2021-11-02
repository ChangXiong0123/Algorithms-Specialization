# Approach: Depth-first search is an algorithm for traversing or searching tree or graph data structures.
# The algorithm starts at the root node
# (selecting some arbitrary node as the root node in the case of a graph)
# and explores as far as possible along each branch before backtracking.
# So the basic idea is to start from the root or any arbitrary node
# and mark the node and move to the adjacent unmarked node
# and continue this loop until there is no unmarked adjacent node.
# Then backtrack and check for other unmarked nodes and traverse them.
# Finally, print the nodes in the path.
from collections import defaultdict


class Graph:
    """
    Algorithm: 
            1.Create a recursive function that takes the index of the node and a visited array.
            2.Mark the current node as visited and print the node.
            3.Traverse all the adjacent and unmarked nodes and call the recursive function 
              with the index of the adjacent node.
            4.Run a loop from 0 to the number of vertices and check if the node is unvisited in the previous DFS, 
              call the recursive function with the current node.
    """

    def __init__(self) -> None:
        self.graph = defaultdict(list)
        self.visited = defaultdict(bool)

    def update_visited(self, node):
        self.visited[node] = True

    def addEdge(self, u, v):
        """add an edge from u to v"""
        self.graph[u].append(v)

    def DFSuntil(self, v):
        # Mark the current node as visited and print it
        self.update_visited(v)
        print(v)
        # Recurse on the edges that are adjacent to this node
        for neighbour in self.graph[v]:
            if self.visited[neighbour] is False:
                self.DFSuntil(neighbour)

    def DFS(self):
        for i in self.graph:
            if self.visited[i] is False:
                self.DFSuntil(i)


g = Graph()
g.addEdge(2, 0)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(0, 1)
g.addEdge(3, 3)
g.DFS()
