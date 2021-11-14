# kosaraju's Two-Pass Algorithm

# DFS + backtraking + Topological

from collections import defaultdict
import sys
import threading
import os
os.chdir('Graph Search, Shortest Paths, and Data Structures/BFS/DFS')


class Graph:
    def __init__(self) -> None:
        self.graph = defaultdict(list)
        self.graph_rev = defaultdict(list)
        self.finish_time_stack = []
        self.visited = defaultdict(bool)
        self.visited_rev = defaultdict(bool)

    def update_visited(self, visit, node):
        """update the visited list
            args:
                visit: either visited_rev or visited
        """
        visit[node] = True

    def read_graph(self, file):
        with open(file) as f:
            for line in f:
                t = line.rstrip()
                fr = t.split()[0]
                to = t.split()[1]
                self.graph[fr].append(to)
                self.graph_rev[to].append(fr)

    def _DFSuntil_rev(self, vertex):
        """recursive subroutione for DSF call"""
        # update the reached node to True in visted status tracker
        self.update_visited(self.visited_rev, vertex)

        for neigbours in self.graph_rev[vertex]:
            if self.visited_rev[neigbours] is False:
                self._DFSuntil_rev(neigbours)
        self.finish_time_stack.append(vertex)

    def _DFSuntil_scc(self, vertex, scc):
        """recursive subroutione for DSF call"""
        # update the reached node to True in visted status tracker
        self.update_visited(self.visited, vertex)
        scc.append(vertex)
        for neigbours in self.graph[vertex]:
            if self.visited[neigbours] is False:
                self._DFSuntil_scc(neigbours, scc)

    def find_finish_time(self):
        for i in list(self.graph_rev.keys()):
            if self.visited_rev[i] is False:
                self._DFSuntil_rev(i)

    def get_scc(self, file):
        self.read_graph(file)
        self.find_finish_time()
        SCC_lst = []
        while self.finish_time_stack:
            # get the vertex by finishing time decending
            # i is the leader
            i = self.finish_time_stack.pop()
            if self.visited[i] is False:
                scc = []
                self._DFSuntil_scc(i, scc)
                SCC_lst.append(scc)
        return SCC_lst


if __name__ == "__main__":
    threading.stack_size(67108864)
    sys.setrecursionlimit(2 ** 20)

    def extract_largest_scc():
        g = Graph()
        SCC_lst = g.get_scc('SCC.txt')
        size = [len(x) for x in SCC_lst]
        size.sort()
        print(size[-5:])
        return size[-5:]

    thread = threading.Thread(target=extract_largest_scc)
    thread.start()
