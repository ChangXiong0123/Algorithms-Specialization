# Dynamic Programing for Knapsack problem

from os import set_inheritable


def read_file(filename):
    """return the value as a list, size as a list, and integer capacity and items of numbers"""
    f = open(filename, 'r').readlines()
    values = [int(x.split()[0]) for x in f[1:]]
    size = [int(x.split()[1]) for x in f[1:]]

    values.insert(0, 0)
    size.insert(0, 0)

    capacity, items_num = int(f[0].split()[0]), int(f[0].split()[1])

    return items_num, capacity, size, values


def knapsack(items, capacity, size, values):
    # use a 2-d array A[item][res_w]
    # res_w denotes residual capacity
    # Initialize A[0,res_w] for res_w =0,1,2,....capacity
    A = [[0]*(capacity+1) for i in range(items+1)]
    for item in range(items+1):
        for res_w in range(capacity+1):
            # deal with the situation where residual capacity res_w < size[item]
            if size[item] > res_w:
                A[item][res_w] = A[item-1][res_w]
            else:
                A[item][res_w] = max(A[item-1][res_w],
                                     A[item-1][res_w-size[item]]+values[item])

    return A


if __name__ == "__main__":

    items_num, capacity, size, values = read_file(
        "Greedy Algorithms, MST, and DP/4/Knapsack/knapsack1.txt")

    A = knapsack(items_num, capacity, size, values)
    print(A[-1][-1])
