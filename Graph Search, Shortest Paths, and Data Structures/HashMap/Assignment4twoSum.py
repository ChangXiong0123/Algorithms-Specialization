# hash table
# import threading
from collections import defaultdict
import os
os.chdir('Graph Search, Shortest Paths, and Data Structures/HashMap')
# design Hashtable

# Bucket the numbers with hash: abs(value) // 10000 into a dictionary using chaining. E.g. hash_table[1234567] = {-12345671111, 12345674544, ...}.

# For each value x, find its hash. From your hash table take all numbers in buckets: (hash, hash-1, hash+1).

# Compute all sums of value x with all the numbers you got from the relevant buckets of the hash table. Add the sum to a set if it's between (-10000) and 10000.

# Return the count of the set of sums.


def read_file(file):
    with open(file) as file:
        lst = [int(x) for x in file]
    return lst


def chain_hash(input_lst):
    chain_hash = defaultdict(list)
    for num in input_lst:
        # adjust to //100000, only need to check number in bucket: (hash)
        chain_hash[abs(num)//100000].append(num)
    return chain_hash


def count_sum(values):
    global sum_set
    for i, num1 in enumerate(values):
        for j, num2 in enumerate(values[i+1:]):
            if num1 != num2:
                sum_set.add(num1+num2)


if __name__ == "__main__":
    lst = read_file('2sum.txt')
    hashes = chain_hash(lst)
    sum_set = set()
    for key, values in hashes.items():
        count_sum(values)

    print(sum([x in range(-10000, 10001) for x in sum_set]))


# too slow using this approach below , need to reconstruct hashmap as mentioned above)

# def TwoSum(input_lst, target):
#     HashMap = {}
#     for num in input_lst:
#         x = target - num
#         if x in HashMap:
#             return target
#         HashMap[num] = num
#     return 0


# def main():
#     target_sum = 0
#     lst = read_file('2sum.txt')
#     hashes = chain_hash(lst)
#     for target in range(-10000, 10001):
#         for key, value in hashes.items():
#             target_sum += TwoSum(value, target)
#     print(target_sum)


# thread = threading.Thread(target=main)
# thread.start()
