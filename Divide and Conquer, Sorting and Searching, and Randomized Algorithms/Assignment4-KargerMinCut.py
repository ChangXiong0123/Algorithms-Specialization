import random
import copy


def read_graph(filename):
    with open(filename) as file:
        graph_dict = {}
        nodes = []
        for line in file:
            t = line.rstrip()
            row = [int(x) for x in t.split()]
            graph_dict[row[0]] = row[1:]
            # nodes.append(row[0])
    return graph_dict

# pick a remaining edges (u,v) uniformly at random


def random_pick(new_dict):
    # choose the node
    u = random.choice(list(new_dict.keys()))
    # choose from the connected nodes with this nodes, the node needs to be merged with u
    v = random.choice(new_dict[u])

    selected_pair = (u, v)

    return selected_pair

# Merge (contract) u and v into a single vertex
# remove single self-loop
# return cut represented by final 2 vertices


def karger(new_dict):
    cut_count = []
    # Merge (contract) u and v into a single vertex
    while len(new_dict) > 2:
        u, v = random_pick(new_dict)
        # add v's connected nodes in dict[u] as they have merged together
        new_dict[u].extend(new_dict[v])

        for c in new_dict[v]:
            # v is merged to u, so any nodes that is connected with v should be connected with u
            new_dict[c].remove(v)
            new_dict[c].append(u)

        # delete self loops in new dict u
        while u in new_dict[u]:
            new_dict[u].remove(u)
        # delete node v(the one was merged)
        del new_dict[v]

    for key in new_dict.keys():
        cut_count.append(len(new_dict[key]))

    return cut_count[0]


def run_karger(n, filename):
    """n: number of ieterations
        filename: read the txt file and out put graph dictionary
    """
    graph = read_graph(filename)
    min_cut = float('inf')
    for i in range(n):
        G = copy.deepcopy(graph)
        cut = karger(G)
        if cut < min_cut:
            min_cut = cut
    return min_cut


file_name = 'kargerMinCut.txt'
t = run_karger(1000, file_name)
print(t)
