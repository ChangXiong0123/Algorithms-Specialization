from heapq import heappush, heappop, heapify
# heappop - pop and return the smallest element from heap
# heappush - push the value item onto the heap, maintaining
#             heap invarient
# heapify - transform list into heap, in place, in linear time


class MinHeap:
    def __init__(self) -> None:
        self.heap = []

    # Parent store in array index (i-1)/2
    def parent(self,i):
        return (i-1)/2

    def insertKey(self,k):
        heappush(self.heap,k)
    
    def extracMin(self):
        return heappop(self.heap)
    
    def deleteKey(self,i):
        self.decreaseKey(i,float("-inf"))
        self.extracMin()
    
    def getMin(self):
        return self.heap[0]
    

    