# Prim's Algorithm without Heap o(mn)
from collections import defaultdict


def read_graph(file):
    graph = defaultdict(list)
    with open(file) as file:
        for position, lines in enumerate(file):
            if position != 0:
                # 1 2 6807, node1, node2, cost
                node1, node2, cost = int(lines.split()[0]), int(
                    lines.split()[1]), int(lines.split()[2])

                graph[node1].append((node2, cost))
                graph[node2].append((node1, cost))
            if position == 0:
                num_nodes, num_edges = int(
                    lines.split()[0]), int(lines.split()[1])
    return graph, num_nodes, num_edges


def prim_mst(graph, num_nodes):
    """run Prim's minimum spanning tree algorithm on this graph.
    Return the overall cost of a minimum spanning tree --- an integer, which may or may not be negative
    """
    x_set = set()
    mst = []
    cost_sum = 0

    # start arbitrarily, set as 1 here
    x_set.add(1)

    while len(x_set) < num_nodes-1:
        min_cost = float('inf')
        min_node = None
        min_edge = ()
        for u in x_set:
            for v in graph[u]:
                if v[0] not in x_set:
                    if v[1] < min_cost:
                        min_cost = v[1]
                        min_node = v[0]
                        min_edge = (u, v[0])
        x_set.add(min_node)
        mst.append(min_edge)
        cost_sum += min_cost
    return cost_sum, mst


graph, num_nodes, num_edges = read_graph(
    'Greedy Algorithms, MST, and DP/1/Greedy/MST/edges.txt')
cost = prim_mst(graph, num_nodes)[0]
print(cost)
