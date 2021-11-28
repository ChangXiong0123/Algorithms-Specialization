# The greedy algorithm on Huffman coding
# Bottom up
# using heap to speed up the runtime

from heapq import heapify, heappop, heappush
from os import read


def read_file(file):
    """"read the file of symbol weights
    return to num_symbols, weights list, elements inside of the list in tuple format: (weight, [symbols])
    """
    weights = []
    num_symbols = 0
    with open(file) as file:
        for position, line in enumerate(file):
            if position == 0:
                num_symbols = int(line)

            elif position != 0:
                # heapify does not support a key function for its ordering
                # mapping the list to tuple(sort_value,list)
                weights.append((int(line), [int(position)]))

    return num_symbols, weights


def greedy_huffman(weights, num_symbols):
    """run the Huffman coding algorithm. 
    return length of a codeword in the resulting Huffman code
    """

    heapify(weights)
    i = 0
    byte = [0]*1000
    while i < num_symbols-1:
        s1 = heappop(weights)
        s2 = heappop(weights)

        w = s1[0]+s2[0]
        meta_nodes = s1[1] + s2[1]
        heappush(weights, (w, meta_nodes))
        i += 1

        for node in meta_nodes:
            byte[node-1] += 1
    return weights, byte


if __name__ == "__main__":

    num_symbols, weights = read_file(
        'Greedy Algorithms, MST, and DP/3/huffmanCode/WIS/huffman.txt')

    new_weights, byte = greedy_huffman(weights, num_symbols)
    print(max(byte), min(byte))


# can implement a node object to store the result as well
# # Creating tree nodes
# class NodeTree(object):
#     def __init__(self, left=None, right=None):
#         self.left = left
#         self.right = right

#     def children(self):
#         return (self.left, self.right)

#     def nodes(self):
#         return (self.left, self.right)

#     def __str__(self):
#         return '%s_%s' % (self.left, self.right)
