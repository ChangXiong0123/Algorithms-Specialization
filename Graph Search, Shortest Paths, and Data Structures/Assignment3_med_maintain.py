# Adding items to the heap using heappush
# function by multiplying them with -1 ---> turn it into Max heap
from heapq import heappop, heappush, heapify, heappushpop
import os
os.chdir('Graph Search, Shortest Paths, and Data Structures')


class maintain_med:
    def __init__(self) -> None:
        # ~i/2 smallest elments in Hlow  - Support extractMAX, MaxHeap, use negative number
        # ~i/2 largest number in Hhigh, support extractMin, minHeap
        self.small, self.large = [], []

    def read_file(self, file, N):
        with open(file) as file:
            lst = [int(next(file)) for x in range(N)]
        return lst

    # metain two heaps, heap_min, heap_max
    # maintain invariant that ~i/2 smallest elments in Hlow, ~i/2 largest number in Hhigh

    def addNum(self, num):
        heappush(self.small, -num)

        # keep all large is larger than small
        if self.small and self.large \
                and (- self.small[0] > self.large[0]):
            heappush(self.large, - heappop(self.small))

        # size difference
        if len(self.small) > len(self.large)+1:
            heappush(self.large, - heappop(self.small))
        elif len(self.large) > len(self.small)+1:
            heappush(self.small, - heappop(self.large))

    def find_med(self):
        if len(self.small) >= len(self.large):
            med = - self.small[0]
        elif len(self.large) > len(self.small):
            med = self.large[0]
        return med


if __name__ == "__main__":

    m = maintain_med()
    med_lst = []
    input_lst = m.read_file('Median.txt', 10000)

    for i in input_lst:
        m.addNum(i)
        med = m.find_med()
        med_lst.append(med)

    print(sum(med_lst))


# def maintain_med(input_lst):
#     small = []  # ~i/2 smallest elments in Hlow  - Support extractMAX, MaxHeap, use negative number
#     large = []  # ~i/2 largest number in Hhigh, support extractMin, minHeap

#     for num in input_lst:
#         if len(small) == len(large):
#             heappush(large, -heappushpop(small, -num))
#         else:
#             heappush(small, -heappushpop(large, num))

#     if len(small) == len(large):
#         return - small[0]
#     else:
#         return large[0]
