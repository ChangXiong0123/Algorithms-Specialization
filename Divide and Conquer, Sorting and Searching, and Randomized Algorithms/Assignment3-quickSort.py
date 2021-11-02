with open('QuickSort.txt') as f:
    raw_data = [int(x) for x in f]

# import sys
# sys.setrecursionlimit(100000)


def partition(arr, left, right, t):
    # p_index = findpivot(arr, type)
    if t == 'f':
        p_index = left
    if t == 'l':
        p_index = right
        arr[p_index], arr[left] = arr[left], arr[p_index]
    if t == 'med':
        # "median-of-three"
        pi = [arr[left], arr[left+(right-left)//2], arr[right]]
        ind = [left, left+(right-left)//2, right]
        x = pi.copy()
        x.remove(min(x))
        x.remove(max(x))
        p_index = ind[pi.index(x[0])]
        arr[p_index], arr[left] = arr[left], arr[p_index]

    p = arr[left]
    i = left+1
    for j in range(left+1, right+1):
        if arr[j] < p:
            arr[i], arr[j] = arr[j], arr[i]
            i = i+1

    # swap the pivot element to the right most of the smaller elements, move pivot to i-1 index
    arr[i-1], arr[left] = arr[left], arr[i-1]

    # i-1 is the partioninig index
    pi = i-1
    # # comparison
    c = right - left
    return pi, c


def qsort(arr, left, right, t):
    c = 0
    nleft = 0
    nright = 0
    if len(arr) == 1:
        return arr
    if left < right:
        pi, c = partition(arr, left, right, t)
        # Separately sort elements before partition and after partition
        nright = qsort(arr, left, pi-1, t)
        nleft = qsort(arr, pi+1, right, t)

    return c+nleft+nright


# arr = [4, 3, 2, 1]
# n = len(arr)
# x = qsort(arr, 0, n, 'f')
# print(arr)
# print(x)

# x = qsort(arr, 0, n, 'l')
# print(arr)
# print(x)

# x = qsort(arr, 0, n, 'med')
# print(arr)
# print(x)

# print(qsort(raw_data, 0, len(raw_data)-1, 'f'))
# print(qsort(raw_data, 0, len(raw_data)-1, 'l'))
print(qsort(raw_data, 0, len(raw_data)-1, 'med'))
