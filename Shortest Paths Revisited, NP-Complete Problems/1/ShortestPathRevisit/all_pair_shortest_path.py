# All pair shortest path
# A Dynamic Programming solution
# The Floyd-Warshall Algorithm


# optimal substructure: Let P be the shortest cycle free i-j path with all internal nodes in V(k)
# Case1: If k not internal to P, then P is the shortest cycle free i-j path with all internal nodes in V(k-1)
# Case2: If k is internal to P, then P1 = shortest(cycle free) i-k path, P2 = shortset k-j path un V(k-1)

# Initialization:
# Let A be a 3-D array(indexed by i,j,k)
# base case: for all i, j belongs to V
# 1. A[i,j,0] = 0 if i=j
# 2.A[i,j,0]= cost_ij if i,j belongs to E
# 3.A[i,j,0]= inf if i!=j and i,j does not internal

# Loop through k, i, j in n, n, n --> A[i,j,k] = min{A[i,j,k-1],A[i,k,k-1] + A[k,j,k-1]}
# How to determine Negative Edges? Scan the Diagonal
# will have at least one i belongs to V: A[i,i,n]<0 at the end of the algo with negative cycles existent

import numpy as np
from tqdm import tqdm


def read_edges(file_name):
    """n = number of nodes, m = number of edges
    return to the initialized 3-D array A"""

    with open(file_name) as f:
        first_row = list(map(int, f.readline().split(' ')))
        n, m = first_row[0], first_row[1]

        A = np.zeros((n, n, n))
        for i in range(n):
            for j in range(n):
                A[i, j, 0] = 0 if i == j else np.inf
        for position, line in enumerate(f):
            if position != 0:
                item = list(map(int, line.split(' ')))
                A[item[0]-1, item[1]-1, 0] = item[2]

    return n, A


def floyd_warshall(A, n):
    """Run Floyd Warshall Algorithm to get the the shortest Path 
    return to the shortest path if no negative cycles exist
    return to string "Negative cycles exists" if negative cycle exists"""

    for k in tqdm(range(1, n)):
        for i in range(n):
            for j in range(n):
                A[i, j, k] = min(A[i, j, k-1], A[i, k-1, k-1] + A[k-1, j, k-1])

    for i in range(n):
        if A[i, i, n-1] < 0:
            return "Negative Cycles Exit"

    return np.min(A[:, :, n-1])


if __name__ == "__main__":

    n, A = read_edges(
        'Shortest Paths Revisited, NP-Complete Problems/1/ShortestPathRevisit/g3.txt')

    min_path = floyd_warshall(A, n)
    print(min_path)
