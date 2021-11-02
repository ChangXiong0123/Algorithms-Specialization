with open('IntegerArray.txt') as f:
    lines = [int(x) for x in f]
# print(lines)
# # print(len(lines))
# # print(type(len(lines)))
# # print(type(len(lines)/2))
# # print(lines[:int(len(lines)/2)])

def merge_sort(input_list):
    n = len(input_list)
    if n==1:
        return input_list
    else:
        R = input_list[:int(n/2)]
        L = input_list[int(n/2):]
        merge_sort(R)
        merge_sort(L)
        i = 0
        j = 0
        k = 0
    # for k in range(n):
    while i < len(R) and j < len(L):
        if R[i] < L[j]:
            input_list[k] = R[i]
            i +=1
        elif R[i] > L[j]:
            input_list[k] = L[j]
            j +=1
        k +=1

        # For all the remaining values
    while i < len(R):
        input_list[k] = R[i]
        i += 1
        k += 1

    while j < len(L):
        input_list[k] = L[j]
        j += 1
        k += 1
        
        
# merge_sort(lines)
# print(lines)

def inversion_count(input_list):
    n = len(input_list)
    # print(n)
    if n == 1:
        count = 0
        return count,input_list
    else:
        R = input_list[:int(n/2)]
        L = input_list[int(n/2):]
        
        x,R = inversion_count(R)
        y,L = inversion_count(L)
        
        temp =[None]*n
        i = 0
        j = 0
        k = 0
        count = 0+x+y
        # count = 0

        while i<len(R) and j<len(L):
            if R[i] < L[j]:
                temp[k] = R[i]
                i +=1
            elif R[i] > L[j]:
                temp[k] = L[j]
                j +=1
                count += (len(R)-i)
            k +=1

        # For all the remaining values
        while i < len(R):
            temp[k] = R[i]
            i += 1
            k += 1

        while j < len(L):
            temp[k] = L[j]
            j += 1
            k += 1
    return count,temp
        # else:
        #     count = 0
        # return count
        
            
   
c,m = inversion_count(lines)
print(c)
print(m)

# def mergeSortInversions(arr):
#     if len(arr) == 1:
#         return arr, 0
#     else:
#         a = arr[:int(len(arr)/2)]
#         b = arr[int(len(arr)/2):]
#         a, ai = mergeSortInversions(a)
#         b, bi = mergeSortInversions(b)
#         c = []
#         i = 0
#         j = 0
#         inversions = 0 + ai + bi
#     while i < len(a) and j < len(b):
#         if a[i] <= b[j]:
#             c.append(a[i])
#             i += 1
#         else:
#             c.append(b[j])
#             j += 1
#             inversions += (len(a)-i)
#     c += a[i:]
#     c += b[j:]
#     return c, inversions

# c,count = mergeSortInversions(lines)
# print(count)

