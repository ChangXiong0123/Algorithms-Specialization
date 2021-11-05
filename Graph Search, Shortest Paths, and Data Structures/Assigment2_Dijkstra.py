# Simple Dijkstra without heap O(mn)
from collections import defaultdict
import os
os.chdir('Graph Search, Shortest Paths, and Data Structures')

graph = defaultdict(list)
with open('dijkstraData.txt') as f:
    for line in f:
        t = line.rstrip().split()
        node = int(t[0])
        edges_dist = [[int(x.split(',')[0]), int(x.split(',')[1])]
                      for x in t[1:]]
        graph[node] = edges_dist


dist = {}
for i in graph:
    dist[i] = 100000

visited = set()

visited.add(1)
dist[1] = 0

while len(visited) < 200:
    s_dist = {}
    for v in visited:
        for w in graph[v]:
            if w[0] not in visited:
                s_dist[(v, w[0])] = dist[v] + w[1]
    (node, edge), dis = min(s_dist.items(), key=lambda x: x[1])
    dist[edge] = dis
    visited.add(edge)

lst = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]
ans = []
for i in lst:
    ans.append(dist[i])

print(ans)
